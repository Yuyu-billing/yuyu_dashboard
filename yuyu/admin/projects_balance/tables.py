from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import tables


class DetailAction(tables.LinkAction):
    name = "detail"
    verbose_name = "Detail"

    def get_link_url(self, datum=None, ):
        return reverse("horizon:admin:projects_balance:balance_detail", kwargs={
            "project_id": datum['project_id'],
        })


class TopUpAction(tables.LinkAction):
    name = "top_up"
    verbose_name = "Top Up"
    icon = "plus"
    classes = ("ajax-modal",)

    def get_link_url(self, datum=None, ):
        return reverse("horizon:admin:projects_balance:top_up", kwargs={
            "project_id": self.table.kwargs['project_id'],
        })


class TopDownAction(tables.LinkAction):
    name = "top_down"
    verbose_name = "Top Down"
    icon = "minus"
    classes = ("ajax-modal",)

    def get_link_url(self, datum=None, ):
        return reverse("horizon:admin:projects_balance:top_down", kwargs={
            "project_id": self.table.kwargs['project_id'],
        })


class BalanceProjectTable(tables.DataTable):
    project = tables.WrappingColumn('project', verbose_name=_('Project'))
    amount = tables.WrappingColumn('amount', verbose_name=_('Amount'))

    def get_object_id(self, datum):
        return datum['id']

    def get_object_display(self, datum):
        return datum['project']

    class Meta(object):
        name = "balance_project_table"
        hidden_title = True
        verbose_name = _("Project Balance")
        row_actions = (DetailAction,)


class BalanceTransactionTable(tables.DataTable):
    date = tables.WrappingColumn('date', verbose_name=_('Date'))
    amount = tables.WrappingColumn('amount', verbose_name=_('Amount'))
    action = tables.Column('action', verbose_name=_('Action'))
    description = tables.Column('description', verbose_name=_('Description'))

    def get_object_id(self, datum):
        return datum['id']

    def get_object_display(self, datum):
        return datum['date']

    class Meta(object):
        name = "balance_table"
        hidden_title = True
        verbose_name = _("Balance Transaction")
        table_actions = (TopUpAction, TopDownAction,)
