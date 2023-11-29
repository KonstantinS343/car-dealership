import pytest

from rest_framework import status

import json

from apps.common.conftest import api_client, user  # noqa
from apps.supplier.tests.conftest import supplier  # noqa


class TestPurchasesSalesHistorySupplier:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/"

    @pytest.mark.parametrize('user_type', [3])
    def test_supplier_history_list(self, user_type, api_client, user, supplier, purchase_history_supplier) -> None:
        response = api_client.get(self.endpoint + f'supplier/{supplier.id}/history/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
