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
    url(r'^(?P<notification_id>[^/]+)/$',
        views.DetailView.as_view(),
        name='detail'),
    url(r'^resend/(?P<notification_id>[^/]+)/$',
        views.ResendView.as_view(),
        name='resend'),
    url(r'^read_all/(?P<selection>[^/]+)$', views.ReadAllView.as_view(), name='read_all'),
]

