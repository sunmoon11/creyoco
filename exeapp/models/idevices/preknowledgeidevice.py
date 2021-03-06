from django.db import models
from django.utils.translation import ugettext_lazy as _
from exeapp.models.idevices.idevice import Idevice
from exeapp.models.idevices import fields
from exeapp.models.idevices.genericidevice import GenericIdevice


class PreknowledgeIdevice(GenericIdevice):
    name = _("Preknowledge")
    title = models.CharField(max_length=100, default=name)
    purpose = _("""Prerequisite knowledge refers to the knowledge learners
    should already have in order to be able to effectively complete the
    learning. Examples of pre-nowledge can be:
    <ul>
        <li>Learners must have level 4 English </li>
        <li>Learners must be able to assemble standard power tools </li>
    </ul>
    """)
    group = Idevice.DIDACTICS
    emphasis = Idevice.SOMEEMPHASIS
    content = fields.RichTextField(blank=True, default="",
           help_text=_("""Describe the prerequisite knowledge learners
                        should have to effectively complete this learning."""))
    icon = "icon_preknowledge.gif"

    class Meta:
        app_label = "exeapp"
