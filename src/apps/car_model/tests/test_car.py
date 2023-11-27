import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ddf import G

import json

from apps.common.models import User
from apps.car_model.models import Car


class TestCar:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/carmodels/"
    CAR_AMOUNT = 10
    AMOUNT_CAR_ATTRIBUTES = 6

    @staticmethod
    def authenticate_client(user) -> APIClient:
        refresh = RefreshToken.for_user(user)
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        return api_client

    @staticmethod
    def init_user() -> User:
        user = G(User)
        return user

    @staticmethod
    def init_car() -> Car:
        car = G(Car)
        return car

    def test_car_list(self) -> None:
        user = self.init_user()
        for i in range(TestCar.CAR_AMOUNT):
            self.init_car()
        api_client = self.authenticate_client(user)

        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestCar.CAR_AMOUNT

    def test_car_retrive(self) -> None:
        user = self.init_user()
        car = self.init_car()
        api_client = self.authenticate_client(user)

        response = api_client.get(self.endpoint + f'{car.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestCar.AMOUNT_CAR_ATTRIBUTES
