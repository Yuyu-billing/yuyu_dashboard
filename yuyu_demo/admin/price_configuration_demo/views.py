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

from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext_lazy as _
from neutronclient.common import exceptions as neutron_exc


from .forms import FlavorPriceForm, VolumePriceForm, FloatingIpPriceForm, RouterPriceForm, SnapshotPriceForm, ImagePriceForm
from .tabs import PriceConfigurationTabs

from ....yuyu.admin.price_configuration import views

class IndexView(views.IndexView):
    tab_group_class = PriceConfigurationTabs
    

class FlavorPriceAddFormView(views.FlavorPriceAddFormView):
    form_class = FlavorPriceForm
    submit_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:flavor_price_create")
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_flavor.html'



class FlavorPriceUpdateFormView(views.FlavorPriceUpdateFormView):
    form_class = FlavorPriceForm
    submit_url = "horizon:yuyu_demo:price_configuration_demo:flavor_price_update"
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_flavor.html'


class VolumePriceAddFormView(views.VolumePriceAddFormView):
    form_class = VolumePriceForm
    submit_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:volume_price_create")
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_volume.html'

  
class VolumePriceUpdateFormView(views.VolumePriceUpdateFormView):
    form_class = VolumePriceForm
    form_id = "volume_price_form_update"
    page_title = _("Volume Price")
    submit_label = _("Update Volume Price")
    submit_url = "horizon:yuyu_demo:price_configuration_demo:volume_price_update"
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_volume.html'

  

class FloatingIpPriceAddFormView(views.FloatingIpPriceAddFormView):
    form_class = FloatingIpPriceForm
  
    submit_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:floating_ip_price_create")
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_floating_ip.html'


class FloatingIpPriceUpdateFormView(views.FloatingIpPriceUpdateFormView):
    form_class = FloatingIpPriceForm
    submit_url = "horizon:yuyu_demo:price_configuration_demo:floating_ip_price_update"
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_floating_ip.html'



class RouterPriceAddFormView(views.RouterPriceAddFormView):
    form_class = RouterPriceForm

    submit_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:router_price_create")
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_router.html'

class RouterPriceUpdateFormView(views.RouterPriceUpdateFormView):
    form_class = RouterPriceForm
    submit_url = "horizon:yuyu_demo:price_configuration_demo:router_price_update"
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_router.html'



class SnapshotPriceAddFormView(views.SnapshotPriceAddFormView):
    form_class = SnapshotPriceForm
    submit_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:snapshot_price_create")
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_snapshot.html'


class SnapshotPriceUpdateFormView(views.SnapshotPriceUpdateFormView):
    form_class = SnapshotPriceForm
    submit_url = "horizon:yuyu_demo:price_configuration_demo:snapshot_price_update"
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_snapshot.html'


class ImagePriceAddFormView(views.ImagePriceAddFormView):
    form_class = ImagePriceForm
    submit_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:image_price_create")
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_image.html'



class ImagePriceUpdateFormView(views.ImagePriceUpdateFormView):
    form_class = ImagePriceForm
    submit_url = "horizon:yuyu_demo:price_configuration_demo:image_price_update"
    success_url = reverse_lazy("horizon:yuyu_demo:price_configuration_demo:index")
    template_name = 'yuyu_demo/price_configuration_demo/create_image.html'