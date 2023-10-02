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
from ....yuyu.admin.notification_center import views


class IndexView(views.IndexView):
    pass


class DetailView(views.DetailView):
    pass

class ReadAllView(views.ReadAllView):

    def get(self, request, *args, **kwargs):
        return shortcuts.redirect("horizon:yuyu_demo:notification_center_demo:index")


class ResendView(views.ResendView):
    def get(self, request, *args, **kwargs):
        return shortcuts.redirect("horizon:yuyu_demo:notification_center_demo:index")
