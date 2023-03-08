from openstack_dashboard.dashboards.yuyu.core import yuyu_client


class BalanceUseCase():
    def list(self, request):
        response = yuyu_client.get(request, f"balance/")

        return response.json()

    def retrieve_by_project(self, request, tenant_id=None):
        if not tenant_id:
            tenant_id = request.user.project_id
        response = yuyu_client.get(request, f"balance/{tenant_id}/retrieve_by_project/")

        if response.status_code == 404:
            return None
        return response.json()

    def transaction_by_project(self, request, tenant_id=None):
        if not tenant_id:
            tenant_id = request.user.project_id
        response = yuyu_client.get(request, f"balance/{tenant_id}/transaction_by_project/")

        if response.status_code == 404:
            return []
        return response.json()

    def top_up(self, request, tenant_id, payload):
        response = yuyu_client.post(request, f"balance/{tenant_id}/top_up_by_project/", payload)
        return response.json()

    def top_down(self, request, tenant_id, payload):
        response = yuyu_client.post(request, f"balance/{tenant_id}/top_down_by_project/", payload)
        return response.json()
