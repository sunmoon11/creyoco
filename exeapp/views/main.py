'''Main view for a user. Handles both GET/POST request and rpc calls'''
from collections import OrderedDict

from django.db.models import Q
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect

from jsonrpc import jsonrpc_method
from exeapp.models.package import PackageOrder
from exeapp.views import upload_file_form
from exeapp.models import Package, User
from exeapp.shortcuts import get_package_by_id_or_error
from exeapp.views.export.exporter_factory import exporter_map


@login_required
def main(request):
    '''Serve the main page with a list of packages.
    TODO: Use a generic view'''
    user = request.user
    order_list = [(order.package, order.sort_order) for order in
                  PackageOrder.objects.filter(
                          Q(user=request.user)
                          | Q(package__collaborators__pk__contains=request.user.pk)
                  ).select_related("package")]
    package_list = [package for package, _ in sorted(order_list, key=lambda k: k[1])]


    exporter_type_title_map = OrderedDict(((export_type, exporter.title)
                                    for export_type, exporter in list(exporter_map.items())))

    form = upload_file_form.UploadFileForm()

    return render_to_response(
        'main.html',
        locals(),
        context_instance=RequestContext(request))


@login_required
def upload_zip(request):
    if upload_file_form.upload_temp_zip(request):
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "Import failed: Wrong type of file")
        return HttpResponseRedirect("/")


@jsonrpc_method('main.create_package', authenticated=True)
def create_package(request, package_name):
    user = User.objects.get(username=request.user.username)
    p = Package.objects.create(title=package_name, user=user)
    return {'id': p.id, 'title': p.title}


@jsonrpc_method('main.delete_package', authenticated=True)
@get_package_by_id_or_error
def delete_package(request, package):
    '''Removes a package'''

    package_id = package.id
    if package.user == request.user:
        package.delete()
        return {"package_id": package_id}
    else:
        return {"package_id": -1}
    package.delete()
    return {"package_id": package_id}


@jsonrpc_method('main.duplicate_package', authenticated=True)
@get_package_by_id_or_error
def duplicate_package(request, package):
    '''Duplicates a package'''
    p = package.duplicate()
    return {"id": p['id'], "title": p['title']}


@jsonrpc_method('main.drag_package', authenticated=True)
@get_package_by_id_or_error
def drag_package(request, package, position):
    pos = PackageOrder.reorder_package(package, request.user, position)
    return {"packageid": package.title, "position": pos}


