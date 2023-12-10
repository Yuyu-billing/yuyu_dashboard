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
from django.utils.timesince import timesince
from django.utils.translation import ugettext_lazy as _
from djmoney.money import Money

from horizon import exceptions, tables, tabs
from openstack_dashboard import api
from openstack_dashboard.dashboards.yuyu.cases.invoice_use_case import InvoiceUseCase
from openstack_dashboard.dashboards.yuyu.cases.setting_use_case import SettingUseCase
from openstack_dashboard.dashboards.yuyu.core.usage_cost.tables import InstanceCostTable, VolumeCostTable, \
    FloatingIpCostTable, RouterCostTable, SnapshotCostTable, ImageCostTable
from openstack_dashboard.dashboards.yuyu.core.usage_cost.tabs import UsageCostTabs


class IndexViewTab(tabs.TabbedTableView):

    tab_group_class = UsageCostTabs
    page_title = _("Usage Cost")
    template_name = "project/usage_cost/index_tabs.html"

    invoice_uc = InvoiceUseCase()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.invoice_list = self.invoice_uc.get_simple_list(self.request)
        request.has_invoice = len(request.invoice_list) != 0

        invoice_id = self.request.GET.get('invoice_id', None)
        if not invoice_id and request.has_invoice:
            invoice_id = request.invoice_list[0]['id']

        request.invoice = self.invoice_uc.get_invoice(self.request, invoice_id) if request.has_invoice else {}
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invoice_list'] = self.request.invoice_list
        context['invoice'] = self.request.invoice
        return context
    

class DownloadView(tables.MultiTableView):
    table_classes = (
        InstanceCostTable, VolumeCostTable, FloatingIpCostTable, RouterCostTable, SnapshotCostTable, ImageCostTable)
    page_title = _("Usage Cost")
    template_name = "project/usage_cost/cost_download.html"

    invoice_uc = InvoiceUseCase()
    setting_uc = SettingUseCase()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.invoice_list = self.invoice_uc.get_simple_list(self.request)
        request.has_invoice = len(request.invoice_list) != 0

        invoice_id = self.request.GET.get('invoice_id', None)
        if not invoice_id and request.has_invoice:
            invoice_id = request.invoice_list[0]['id']

        request.invoice = self.invoice_uc.get_invoice(self.request, invoice_id) if request.has_invoice else {}
        return super(DownloadView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invoice_list'] = self.request.invoice_list
        context['invoice'] = self.request.invoice
        context['setting'] = self.setting_uc.get_settings(self.request)
        
        return context

    def _get_flavor_name(self, flavor_id):
        try:
            return api.nova.flavor_get(self.request, flavor_id).name
        except Exception:
            return 'Invalid Flavor'

    def get_instance_cost_data(self):
        try:
            datas = map(lambda x: {
                "id": x['id'],
                "name": x['name'],
                "flavor": self._get_flavor_name(x['flavor_id']),
                "usage": timesince(
                    dateutil.parser.isoparse(x['start_date']),
                    dateutil.parser.isoparse(x['adjusted_end_date'])
                ),
                "cost": Money(amount=x['price_charged'], currency=x['price_charged_currency'])
            }, self.request.invoice.get('instances', []))

            return datas
        except Exception:
            error_message = _('Unable to get instance cost')
            exceptions.handle(self.request, error_message)

            return []

    def _get_volume_name(self, volume_type_id):
        try:
            return api.cinder.volume_type_get(self.request, volume_type_id).name
        except Exception:
            return 'Invalid Volume'

    def get_volume_cost_data(self):
        try:
            datas = map(lambda x: {
                "id": x['id'],
                "name": x['volume_name'],
                "usage": timesince(
                    dateutil.parser.isoparse(x['start_date']),
                    dateutil.parser.isoparse(x['adjusted_end_date'])
                ),
                'type': self._get_volume_name(x['volume_type_id']),
                'size': x['space_allocation_gb'],
                "cost": Money(amount=x['price_charged'], currency=x['price_charged_currency'])
            }, self.request.invoice.get('volumes', []))
            return datas
        except Exception:
            error_message = _('Unable to get volume cost')
            exceptions.handle(self.request, error_message)

            return []

    def get_floating_ip_cost_data(self):
        try:
            datas = map(lambda x: {
                "id": x['id'],
                "name": x['ip'],
                "usage": timesince(
                    dateutil.parser.isoparse(x['start_date']),
                    dateutil.parser.isoparse(x['adjusted_end_date'])
                ),
                "cost": Money(amount=x['price_charged'], currency=x['price_charged_currency'])
            }, self.request.invoice.get('floating_ips', []))

            return datas
        except Exception:
            error_message = _('Unable to get floating ip cost')
            exceptions.handle(self.request, error_message)

            return []

    def get_router_cost_data(self):
        try:
            datas = map(lambda x: {
                "id": x['id'],
                "name": x['name'],
                "usage": timesince(
                    dateutil.parser.isoparse(x['start_date']),
                    dateutil.parser.isoparse(x['adjusted_end_date'])
                ),
                "cost": Money(amount=x['price_charged'], currency=x['price_charged_currency'])
            }, self.request.invoice.get('routers', []))

            return datas
        except Exception:
            error_message = _('Unable to get router cost')
            exceptions.handle(self.request, error_message)

            return []

    def get_snapshot_cost_data(self):
        try:
            datas = map(lambda x: {
                "id": x['id'],
                "name": x['name'],
                'size': x['space_allocation_gb'],
                "usage": timesince(
                    dateutil.parser.isoparse(x['start_date']),
                    dateutil.parser.isoparse(x['adjusted_end_date'])
                ),
                "cost": Money(amount=x['price_charged'], currency=x['price_charged_currency'])
            }, self.request.invoice.get('snapshots', []))

            return datas
        except Exception:
            error_message = _('Unable to get snapshot cost')
            exceptions.handle(self.request, error_message)

            return []

    def get_image_cost_data(self):
        try:
            datas = map(lambda x: {
                "id": x['id'],
                "name": x['name'],
                'size': x['space_allocation_gb'],
                "usage": timesince(
                    dateutil.parser.isoparse(x['start_date']),
                    dateutil.parser.isoparse(x['adjusted_end_date'])
                ),
                "cost": Money(amount=x['price_charged'], currency=x['price_charged_currency'])
            }, self.request.invoice.get('images', []))

            return datas
        except Exception:
            error_message = _('Unable to get images cost')
            exceptions.handle(self.request, error_message)

            return []
