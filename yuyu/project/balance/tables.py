from django.utils.translation import ugettext_lazy as _

from horizon import tables


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
