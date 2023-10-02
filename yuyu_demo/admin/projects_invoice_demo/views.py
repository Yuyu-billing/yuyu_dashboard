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

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import views

from .tables import InvoiceTable

from ....yuyu.admin.projects_invoice import views

class IndexView(views.IndexView):
    table_class = InvoiceTable

class InvoiceView(views.InvoiceView):
   pass

class UsageCostTabView(views.UsageCostTabView):
   pass

class UsageCostView(views.UsageCostView):
    pass


class FinishInvoice(views.FinishInvoice):
    def get(self, request, *args, **kwargs):
        next_url = request.GET.get('next', reverse('horizon:yuyu_demo:projects_invoice_demo:index'))
        return HttpResponseRedirect(next_url)


class RollbackToUnpaidInvoice(views.RollbackToUnpaidInvoice):
    def get(self, request, *args, **kwargs):
        next_url = request.GET.get('next', reverse('horizon:yuyu_demo:projects_invoice_demo:index'))
        return HttpResponseRedirect(next_url)
