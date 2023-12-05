import pytest

from rest_framework import status

import json

from apps.common.conftest import api_client, user  # noqa
from apps.supplier.tests.conftest import supplier  # noqa


class TestPurchasesSalesHistorySupplier:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/"

    @pytest.mark.parametrize('user_type, model', [(3, 'audi')])
    def test_supplier_history_list(self, user_type, api_client, user, supplier, purchase_history_supplier) -> None:
        response = api_client.get(self.endpoint + f'supplier/{supplier.id}/history/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type, model', [(3, 'audi')])
    def test_supplier_filter_queryset(self, user_type, api_client, supplier, purchase_history_supplier, model) -> None:
        response = api_client.get(self.endpoint + f'supplier/{supplier.id}/history/?car_model={model}')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
