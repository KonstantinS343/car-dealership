import pytest

from rest_framework import status

import json

from apps.common.conftest import api_client, user  # noqa


class TestBuyerStatistics:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/buyer/"

    @pytest.mark.parametrize('user_type', [1])
    def test_statistics_buyer_profit(self, user_type, api_client, buyer, buyer_history) -> None:
        response = api_client.get(self.endpoint + f'{buyer.id}/statistics/profit/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [1])
    def test_statistics_buyer_cars_sold(self, user_type, api_client, buyer, buyer_history) -> None:
        response = api_client.get(self.endpoint + f'{buyer.id}/statistics/cars/bought/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [1])
    def test_statistics_buyer_cars_sold_profit(self, user_type, api_client, buyer, buyer_history) -> None:
        response = api_client.get(self.endpoint + f'{buyer.id}/statistics/cars/bought/expenses/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
