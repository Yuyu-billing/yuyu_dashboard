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
from django.urls import reverse_lazy, reverse
from django.utils import formats
from django.utils.translation import ugettext_lazy as _
from djmoney.money import Money

from horizon import exceptions, forms
from horizon import tables
from openstack_dashboard import api
from .forms import TopUpForm, TopDownForm
from .tables import BalanceProjectTable, BalanceTransactionTable
from ...cases.balance_use_case import BalanceUseCase
from keystoneclient import exceptions as keystone_exceptions


class IndexView(tables.DataTableView):
    table_class = BalanceProjectTable
    page_title = _("Balance")
    template_name = "admin/projects_balance/balance_projects.html"

    balance_uc = BalanceUseCase()

    def get_data(self):
        try:
            data = []
            project_list, has_more = api.keystone.tenant_list(self.request)
            for d in self.balance_uc.list(self.request):
                project = list(filter(lambda x: x.id == d['project']['tenant_id'], project_list))
                project_name = 'Unknown Project'
                project_id = 'invalid'
                if len(project) > 0:
                    project_name = project[0].name
                    project_id = project[0].id

                data.append({
                    'id': d['id'],
                    'project_id': project_id,
                    'project': project_name,
                    'amount': Money(amount=d['amount'], currency=d['amount_currency']),
                })
            return list(data)
        except Exception as e:
            error_message = _('Unable to get balance')
            exceptions.handle(self.request, error_message)


class DetailBalanceView(tables.DataTableView):
    table_class = BalanceTransactionTable
    template_name = "admin/projects_balance/balance_table.html"

    balance_uc = BalanceUseCase()

    def get_context_data(self, **kwargs):
        project_id = self.kwargs['project_id']
        balance = self.balance_uc.retrieve_by_project(self.request, project_id)
        try:
            project = api.keystone.tenant_get(self.request, project_id)
        except keystone_exceptions.NotFound:
            project = 'Unknown'

        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Project {project.name} Balance'
        context['amount'] = Money(amount=balance['amount'], currency=balance['amount_currency']) if balance else 0
        return context

    def get_data(self):
        project_id = self.kwargs['project_id']
        data = []

        for d in self.balance_uc.transaction_by_project(self.request, project_id):
            data.append({
                'id': d['id'],
                'date': formats.date_format(dateutil.parser.isoparse(d['created_at']), 'd M Y H:m'),
                'amount': Money(amount=d['amount'], currency=d['amount_currency']),
                'action': d['action'],
                'description': d['description'],
            })
        return list(data)


class TopUpView(forms.ModalFormView):
    form_class = TopUpForm
    form_id = "top_up_form"
    modal_id = "top_up_modal"
    modal_header = _("Top Up")
    page_title = _("Top Up")
    submit_label = _("Top Up")
    template_name = 'admin/projects_balance/form_top_up.html'

    def get_form_kwargs(self):
        kwargs = super(TopUpView, self).get_form_kwargs()
        kwargs['project_id'] = self.kwargs['project_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(TopUpView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('horizon:admin:projects_balance:top_up', kwargs={
            'project_id': self.kwargs['project_id']
        })
        return context

    def get_success_url(self):
        return reverse('horizon:admin:projects_balance:balance_detail', kwargs={
            'project_id': self.kwargs['project_id']
        })


class TopDownView(forms.ModalFormView):
    form_class = TopDownForm
    form_id = "top_down_form"
    modal_id = "top_down_modal"
    modal_header = _("Top Down")
    page_title = _("Top Down")
    submit_label = _("Top Down")
    template_name = 'admin/projects_balance/form_top_down.html'

    def get_form_kwargs(self):
        kwargs = super(TopDownView, self).get_form_kwargs()
        kwargs['project_id'] = self.kwargs['project_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(TopDownView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('horizon:admin:projects_balance:top_down', kwargs={
            'project_id': self.kwargs['project_id']
        })
        return context

    def get_success_url(self):
        return reverse('horizon:admin:projects_balance:balance_detail', kwargs={
            'project_id': self.kwargs['project_id']
        })

