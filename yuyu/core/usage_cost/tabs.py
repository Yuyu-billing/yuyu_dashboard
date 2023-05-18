import dateutil.parser
from django.utils.timesince import timesince
from django.utils.translation import ugettext_lazy as _
from djmoney.money import Money

from horizon import exceptions, tabs
from openstack_dashboard import api
from openstack_dashboard.dashboards.yuyu.core.usage_cost.tables import (
    InstanceCostTable, VolumeCostTable, FloatingIpCostTable, RouterCostTable, SnapshotCostTable, ImageCostTable
)


class InstanceTab(tabs.TableTab):
    table_classes = (InstanceCostTable,)
    name = _("Instance")
    slug = "instance"
    template_name = 'horizon/common/_detail_table.html'

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


class VolumeTab(tabs.TableTab):
    table_classes = (VolumeCostTable,)
    name = _("Volume")
    slug = "volume"
    template_name = 'horizon/common/_detail_table.html'

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


class FloatingIpTab(tabs.TableTab):
    table_classes = (FloatingIpCostTable,)
    name = _("Floating IP")
    slug = "floating_ip"
    template_name = 'horizon/common/_detail_table.html'

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


class RouterTab(tabs.TableTab):
    table_classes = (RouterCostTable,)
    name = _("Router")
    slug = "router"
    template_name = 'horizon/common/_detail_table.html'

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


class SnapshotTab(tabs.TableTab):
    table_classes = (SnapshotCostTable,)
    name = _("Snapshot")
    slug = "snapshot"
    template_name = 'horizon/common/_detail_table.html'

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


class ImageTab(tabs.TableTab):
    table_classes = (ImageCostTable,)
    name = _("Image")
    slug = "image"
    template_name = 'horizon/common/_detail_table.html'

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


class UsageCostTabs(tabs.TabGroup):
    slug = "usage_cost"
    tabs = (InstanceTab, VolumeTab, FloatingIpTab, RouterTab, SnapshotTab, ImageTab, )
    sticky = True
