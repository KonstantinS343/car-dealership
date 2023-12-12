import pytest

from rest_framework import status

import json

from apps.common.conftest import api_client, user  # noqa


class TestSupplierStatistics:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/supplier/"

    @pytest.mark.parametrize('user_type', [3])
    def test_statistics_supplier_profit(self, user_type, api_client, supplier, supplier_history) -> None:
        response = api_client.get(self.endpoint + f'{supplier.id}/statistics/profit/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [3])
    def test_statistics_supplier_cars_sold(self, user_type, api_client, supplier, supplier_history) -> None:
        response = api_client.get(self.endpoint + f'{supplier.id}/statistics/cars/sold/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [3])
    def test_statistics_supplier_cars_sold_profit(self, user_type, api_client, supplier, supplier_history) -> None:
        response = api_client.get(self.endpoint + f'{supplier.id}/statistics/cars/sold/profit/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
