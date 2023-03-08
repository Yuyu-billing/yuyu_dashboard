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

from openstack_dashboard.dashboards.yuyu.admin.projects_balance import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<project_id>[^/]+)/$', views.DetailBalanceView.as_view(), name='balance_detail'),
    url(r'^detail/(?P<project_id>[^/]+)/topup/$',
        views.TopUpView.as_view(), name='top_up'),
    url(r'^detail/(?P<project_id>[^/]+)/top_down/$',
        views.TopDownView.as_view(), name='top_down'),
]
