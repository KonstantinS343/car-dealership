import pytest

from rest_framework import status

import json

from apps.common.conftest import api_client, user  # noqa


class TestCar:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/carmodels/"
    AMOUNT_CAR_ATTRIBUTES = 6

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_car_list(self, user_type, api_client, car) -> None:
        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_car_retrive(self, user_type, api_client, car) -> None:
        response = api_client.get(self.endpoint + f'{car.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestCar.AMOUNT_CAR_ATTRIBUTES
