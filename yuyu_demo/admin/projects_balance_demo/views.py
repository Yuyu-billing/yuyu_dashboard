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
from .forms import TopUpForm, TopDownForm
from .tables import BalanceProjectTable, BalanceTransactionTable

from ....yuyu.admin.projects_balance import views

class IndexView(views.IndexView):
    table_class = BalanceProjectTable

class DetailBalanceView(views.DetailBalanceView):
    table_class = BalanceTransactionTable


class TopUpView(views.TopDownView):
    form_class = TopUpForm
    template_name = 'yuyu_demo/projects_balance_demo/form_top_up.html'

    def get_form_kwargs(self):
        kwargs = super(TopUpView, self).get_form_kwargs()
        kwargs['project_id'] = self.kwargs['project_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(TopUpView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('horizon:yuyu_demo:projects_balance_demo:top_up', kwargs={
            'project_id': self.kwargs['project_id']
        })
        return context

    def get_success_url(self):
        return reverse('horizon:yuyu_demo:projects_balance_demo:balance_detail', kwargs={
            'project_id': self.kwargs['project_id']
        })


class TopDownView(views.TopDownView):
    form_class = TopDownForm
    template_name = 'yuyu_demo/projects_balance_demo/form_top_down.html'

    def get_form_kwargs(self):
        kwargs = super(TopDownView, self).get_form_kwargs()
        kwargs['project_id'] = self.kwargs['project_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(TopDownView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('horizon:yuyu_demo:projects_balance_demo:top_down', kwargs={
            'project_id': self.kwargs['project_id']
        })
        return context

    def get_success_url(self):
        return reverse('horizon:yuyu_demo:projects_balance_demo:balance_detail', kwargs={
            'project_id': self.kwargs['project_id']
        })

