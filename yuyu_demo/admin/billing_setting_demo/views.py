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
from django import shortcuts

from ....yuyu.admin.billing_setting import views
from . import forms

class IndexView(views.IndexView):
    pass


class UpdateSettingView(views.UpdateSettingView):
    form_class = forms.SettingForm
    submit_url = ''
    success_url = ''
    template_name = 'yuyu_demo/billing_setting_demo/form_setting.html'



class EnableBillingView(views.EnableBillingView):
    def get(self, request, *args, **kwargs):
        return shortcuts.redirect("horizon:yuyu_demo:billing_setting_demo:index")


class DisableBillingView(views.DisableBillingView):
    def get(self, request, *args, **kwargs):
        return shortcuts.redirect("horizon:yuyu_demo:billing_setting_demo:index")


class ResetBillingView(views.ResetBillingView):
    def get(self, request, *args, **kwargs):
        return shortcuts.redirect("horizon:yuyu_demo:billing_setting_demo:index")
