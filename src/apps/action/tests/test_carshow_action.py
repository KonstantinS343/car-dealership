import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ddf import G, N
from django.forms.models import model_to_dict

import json

from apps.common.models import User
from apps.car_show.models import CarShow
from apps.action.models import ActionCarDealership


class TestActionCarShow:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/actions/carshow/"
    USER_TYPE = 2
    AMOUNT_ACTION_ATTRIBUTES = 7

    @staticmethod
    def authenticate_client(user) -> APIClient:
        refresh = RefreshToken.for_user(user)
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        return api_client

    @staticmethod
    def init_user(user_type=USER_TYPE) -> User:
        user = G(User, user_type=user_type)
        return user

    @staticmethod
    def init_action(user) -> ActionCarDealership:
        carshow_action = G(ActionCarDealership, car_dealership=G(CarShow, user=user))
        return carshow_action

    def test_list(self) -> None:
        user = self.init_user()
        _ = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    def test_retrive(self) -> None:
        user = self.init_user()
        action = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.get(f'{self.endpoint}{action.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestActionCarShow.AMOUNT_ACTION_ATTRIBUTES

    def test_create(self) -> None:
        user = self.init_user()
        carshow = G(CarShow)
        action = N(ActionCarDealership, car_dealership=carshow, discount=0.4)
        api_client = self.authenticate_client(user)

        response = api_client.post(f"{self.endpoint}", model_to_dict(action))

        assert response.status_code == status.HTTP_201_CREATED

    def test_wrong_create(self) -> None:
        user = self.init_user(user_type=3)
        carshow = G(CarShow)
        action = N(ActionCarDealership, car_dealership=carshow, discount=0.4)
        api_client = self.authenticate_client(user)

        response = api_client.post(f"{self.endpoint}", model_to_dict(action))

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete(self) -> None:
        user = self.init_user()
        action = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.delete(f"{self.endpoint}{action.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_wrong_delete(self) -> None:
        user = self.init_user(user_type=3)
        action = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.delete(f"{self.endpoint}{action.id}/")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update(self) -> None:
        user = self.init_user()
        action = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "name": 'Test',
            "descritpion": 'Test',
            "event_start": '2023-11-11',
            "event_end": '2023-12-12',
            "discount": 0.3,
        }

        response = api_client.put(f"{self.endpoint}{action.id}/", new_data, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_wrong_update(self) -> None:
        user = self.init_user(user_type=3)
        action = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "name": 'Test',
            "descritpion": 'Test',
            "event_start": '2023-11-11',
            "event_end": '2023-12-12',
            "discount": 0.3,
        }

        response = api_client.put(f"{self.endpoint}{action.id}/", new_data, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_partial_update(self) -> None:
        user = self.init_user()
        action = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "name": 'Test',
            "discount": 0.3,
        }

        response = api_client.patch(f"{self.endpoint}{action.id}/", new_data, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_wrong_partial_update(self) -> None:
        user = self.init_user(user_type=1)
        action = self.init_action(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "name": 'Test',
            "discount": 0.3,
        }

        response = api_client.patch(f"{self.endpoint}{action.id}/", new_data, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN
