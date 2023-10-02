from django.utils.translation import ugettext_lazy as _

from horizon import forms

from ....yuyu.admin.price_configuration import forms

class FlavorPriceForm(forms.FlavorPriceForm):
    def handle(self, request, data):
        return



class VolumePriceForm(forms.VolumePriceForm):
    def handle(self, request, data):
        return


class FloatingIpPriceForm(forms.FloatingIpPriceForm):
   def handle(self, request, data):
        return


class RouterPriceForm(forms.RouterPriceForm):
    def handle(self, request, data):
        return


class SnapshotPriceForm(forms.SnapshotPriceForm):
    def handle(self, request, data):
        return

class ImagePriceForm(forms.SnapshotPriceForm):
    def handle(self, request, data):
        return