import base64

from django.core import validators
from django.utils.translation import ugettext_lazy as _
from djmoney.forms import MoneyField

from horizon import forms, messages, exceptions
from openstack_dashboard.dashboards.yuyu.cases.balance_use_case import BalanceUseCase
from openstack_dashboard.dashboards.yuyu.cases.setting_use_case import SettingUseCase


class TopUpForm(forms.SelfHandlingForm):
    USE_CASE = BalanceUseCase()

    amount = MoneyField(label=_("Amount"), min_value=0, max_digits=10)
    description = forms.CharField(label=_("Description"))

    def __init__(self, request, *args, **kwargs):
        self.project_id = kwargs['project_id']
        del kwargs['project_id']
        super().__init__(request, *args, **kwargs)

    def handle(self, request, data):
        try:
            payload = {
                "amount": data['amount'].amount,
                "amount_currency": data['amount'].currency.code,
                'description': data['description'],
            }

            result = self.USE_CASE.top_up(request, self.project_id, payload)
            messages.success(request, _(f"Successfully Top Up"))

            return result
        except Exception as e:
            exceptions.handle(request,
                              _('Unable to top up.'))


class TopDownForm(forms.SelfHandlingForm):
    USE_CASE = BalanceUseCase()

    amount = MoneyField(label=_("Amount"), min_value=0, max_digits=10)
    description = forms.CharField(label=_("Description"))

    def __init__(self, request, *args, **kwargs):
        self.project_id = kwargs['project_id']
        del kwargs['project_id']
        super().__init__(request, *args, **kwargs)

    def handle(self, request, data):
        try:
            payload = {
                "amount": data['amount'].amount,
                "amount_currency": data['amount'].currency.code,
                'description': data['description'],
            }

            result = self.USE_CASE.top_down(request, self.project_id, payload)
            messages.success(request, _(f"Successfully Top Down"))

            return result
        except Exception as e:
            exceptions.handle(request,
                              _('Unable to top down.'))
