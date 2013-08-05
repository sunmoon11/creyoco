from django.db import models
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField
from exeapp.models.idevices.idevice import Idevice

class PDFIdevice(Idevice):


    name = _("Pdf iDevice")
    title = name #models.CharField(max_length=100, default=name)
    author = _("Technical University Munich")
    purpose = _('''Import local pdf and display them.
    Requires Acrobat Reader plugin.''')
    #pdf_file = models.CharField(max_length=100, blank=True, default="")
    pdf_file = FileBrowseField("PDF", max_length=100,
                               directory="pdf/", extensions=['.pdf'],
                               blank=True, null=True)

    #height = models.PositiveIntegerField()
    page_list = models.CharField(max_length=50, blank=True, default="",
                        help_text=_("Input coma-separated pages or page ranges"
                                    "to import. For example: 1,2,3-8. Leave "
                                    "empty to import all pages"))
    group = Idevice.CONTENT
    emphasis = Idevice.NOEMPHASIS

    def _resources(self):
        user = self.parent_node.package.user.username
        return set([self.pdf_file.path_relative_directory.replace("%s/" % user,
                                                                 "")])

    class Meta:
        app_label = "exeapp"