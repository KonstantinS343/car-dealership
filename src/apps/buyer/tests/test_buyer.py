import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ddf import G, N
from django.forms.models import model_to_dict

import json

from apps.common.models import User
from apps.buyer.models import Buyer


class TestBuyer:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/buyer/"
    USER_TYPE = 1
    AMOUNT_BUYER_ATTRIBUTES = 2

    @staticmethod
    def authenticate_client(user) -> APIClient:
        refresh = RefreshToken.for_user(user)
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        return api_client

    @staticmethod
    def init_user() -> User:
        user = G(User, user_type=TestBuyer.USER_TYPE)
        return user

    @staticmethod
    def init_buyer(user) -> Buyer:
        buyer = G(Buyer, user=user)
        return buyer

    def test_list(self) -> None:
        user = self.init_user()
        _ = self.init_buyer(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    def test_retrive(self) -> None:
        user = self.init_user()
        buyer = self.init_buyer(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.get(f'{self.endpoint}{buyer.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestBuyer.AMOUNT_BUYER_ATTRIBUTES

    def test_create(self) -> None:
        user = self.init_user()
        buyer = N(Buyer, user=user)
        api_client = self.authenticate_client(user)

        response = api_client.post(f"{self.endpoint}", model_to_dict(buyer))

        assert response.status_code == status.HTTP_201_CREATED

    def test_delete(self) -> None:
        user = self.init_user()
        buyer = self.init_buyer(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.delete(f"{self.endpoint}{buyer.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update(self) -> None:
        user = self.init_user()
        buyer = self.init_buyer(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "first_name": 'TestName',
            "last_name": 'TestLastName',
        }

        response = api_client.put(f"{self.endpoint}{buyer.id}/", new_data, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_partial_update(self) -> None:
        user = self.init_user()
        buyer = self.init_buyer(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "first_name": 'TestName',
        }

        response = api_client.patch(f"{self.endpoint}{buyer.id}/", new_data, format="json")
        assert response.status_code == status.HTTP_200_OK
