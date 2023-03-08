# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import dateutil.parser
from django.utils import formats
from django.utils.translation import ugettext_lazy as _
from djmoney.money import Money

from horizon import exceptions
from horizon import tables
from .tables import BalanceTransactionTable
from ...cases.balance_use_case import BalanceUseCase
from ...cases.setting_use_case import SettingUseCase


class IndexView(tables.DataTableView):
    table_class = BalanceTransactionTable
    page_title = _("Balance")
    template_name = "project/balance/balance_table.html"

    balance_uc = BalanceUseCase()
    setting_uc = SettingUseCase()

    def get_context_data(self, **kwargs):
        balance = self.balance_uc.retrieve_by_project(self.request)

        context = super().get_context_data(**kwargs)
        context['amount'] = Money(amount=balance['amount'], currency=balance['amount_currency']) if balance else 0
        context['how_to_top_up'] = self.setting_uc.get_setting(self.request, 'how_to_top_up')
        return context

    def get_data(self):
        data = []

        for d in self.balance_uc.transaction_by_project(self.request):
            data.append({
                'id': d['id'],
                'date': formats.date_format(dateutil.parser.isoparse(d['created_at']), 'd M Y H:m'),
                'amount': Money(amount=d['amount'], currency=d['amount_currency']),
                'action': d['action'],
                'description': d['description'],
            })
        return list(data)
