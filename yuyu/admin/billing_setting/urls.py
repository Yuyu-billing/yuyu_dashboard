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

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^enable_billing$', views.EnableBillingView.as_view(), name='enable_billing'),
    url(r'^disable_billing$', views.DisableBillingView.as_view(), name='disable_billing'),
    url(r'^reset_billing$', views.ResetBillingView.as_view(), name='reset_billing'),
    url(r'^reset_transaction$', views.ResetTransactionView.as_view(), name='reset_transaction'),
    url(r'^update_setting/$',
        views.UpdateSettingView.as_view(), name='update_setting'),
]

