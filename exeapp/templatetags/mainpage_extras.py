from __future__ import print_function
from collections import defaultdict
from logging import getLogger
import os

from django.template.defaultfilters import unordered_list
from django.template.loader import render_to_string
from django import template
from django.conf import settings
from django.utils.encoding import force_text

from exeapp.models.idevices.idevice import Idevice


log = getLogger()
register = template.Library()


@register.filter(is_safe=True)
def idevice_ul(groups, group_order):
    idevice_list = []
    for group in group_order:
        idevice_list.append(force_text("<a>%s</a>" % group))
        prototype_list = []
        for prototype in groups[group]:
            prototype_list.append(force_text('<a class="ideviceItem" href="#"' + \
                                  ' ideviceid="%s">%s</a>' % (
                                      prototype.__name__,
                                      force_text(prototype.name))))
        idevice_list.append(prototype_list)
    return unordered_list(idevice_list, autoescape=False)


@register.inclusion_tag('exe/outlinepane.html')
def render_outline(package, current_node):
    NODE_TEMPLATE = "exe/node_link.html"

    node_list = [render_to_string(NODE_TEMPLATE, {"node": package.root}),
                 _create_children_list(package.root, NODE_TEMPLATE)]
    node_list_content = unordered_list(node_list, autoescape=False)

    return locals()


@register.tag
def testing(parser, token):
    '''Show content of a tag only if settings.DEBUG is set'''
    nodelist = parser.parse(('endtesting',))
    parser.delete_first_token()
    if settings.DEBUG:
        return TestingNode(nodelist)
    else:
        return TestingNode()


class TestingNode(template.Node):
    '''Renders nodes, if there are any'''

    def __init__(self, nodelist=None):
        self.nodelist = nodelist

    def render(self, context):
        if self.nodelist is not None:
            return self.nodelist.render(context)
        else:
            return ""


@register.inclusion_tag('exe/idevicepane.html')
def render_idevicepane(idevices):
    """
    Returns an html string for viewing idevicepane
    """

    groups = defaultdict(list)

    idevices.sort(key=lambda x: x.name)
    for idevice in idevices:
        if idevice.group:
            groups[idevice.group].append(idevice)
        else:
            groups[Idevice.UNKNOWN] += idevice

    group_order = (group for group in Idevice.GROUP_ORDER \
                   if group in groups)
    return locals()


@register.inclusion_tag("exe/styles.html")
def render_styles():
    styles = sorted([os.path.basename(style) for style in \
                     os.listdir(settings.STYLE_DIR) \
                     # style dir has to be joined because of a bug on windows
                     # with abapath resolving
                     if os.path.isdir(os.path.join(settings.STYLE_DIR, style))])
    return locals()


def _create_children_list(node, template=None, ):
    """Creates a list of all children from the root recursively.
Root node has to be appended manually in a higher level function. List items
will
be rendered using given template. """
    children_list = []

    if node.children.exists():
        for child in node.children.all():
            if template is None:
                node_item = child.title
            else:
                node_item = render_to_string(template, {"node": child})
            children_list.append(node_item)
            if child.children.exists():
                children_list.append(_create_children_list(child,
                                                           template))
            else:
                children_list.append([])
    return children_list
