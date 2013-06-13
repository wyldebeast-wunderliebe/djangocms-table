from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


class Table(CMSPlugin):
    """
    Table plugin
    """

    name = models.CharField(_("name"), max_length=256)

    headers_top = models.PositiveSmallIntegerField(_("top"), default=1)
    headers_left = models.PositiveSmallIntegerField(_("left"), default=0)
    headers_bottom = models.PositiveSmallIntegerField(_("bottom"), default=0)
    cssclass = models.CharField(
        _("CSS class"),
        help_text=_("You can use classes for styling purposes like e.g. "
                    "'table table-striped'."),
        max_length=100, blank=True, null=True)
    table_data = models.TextField(_("table data"))

    def __unicode__(self):
        return self.name

    search_fields = ('name', 'table_data')
