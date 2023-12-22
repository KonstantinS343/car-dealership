import pytest

from rest_framework import status

import json

from apps.common.conftest import api_client, user  # noqa


class TestCarShowStatistics:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/carshow/"

    @pytest.mark.parametrize('user_type', [2])
    def test_statistics_carshow_profit(self, user_type, api_client, carshow, carshow_history) -> None:
        response = api_client.get(self.endpoint + f'{carshow.id}/statistics/profit/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [2])
    def test_statistics_carshow_cars_sold(self, user_type, api_client, carshow, carshow_history) -> None:
        response = api_client.get(self.endpoint + f'{carshow.id}/statistics/cars/sold/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [2])
    def test_statistics_carshow_cars_sold_profit(self, user_type, api_client, carshow, carshow_history) -> None:
        response = api_client.get(self.endpoint + f'{carshow.id}/statistics/cars/sold/profit/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
