import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ddf import G, N
from django.forms.models import model_to_dict

import json

from apps.common.models import User
from apps.supplier.models import Supplier


class TestSupplier:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/supplier/"
    USER_TYPE = 3

    @staticmethod
    def authenticate_client(user) -> APIClient:
        refresh = RefreshToken.for_user(user)
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        return api_client

    @staticmethod
    def init_user() -> User:
        user = G(User, user_type=TestSupplier.USER_TYPE)
        return user

    @staticmethod
    def init_supplier(user) -> Supplier:
        supplier = G(Supplier, user=user)
        return supplier

    def test_list(self) -> None:
        user = self.init_user()
        _ = self.init_supplier(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_retrive(self) -> None:
        user = self.init_user()
        supplier = self.init_supplier(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.get(f'{self.endpoint}{supplier.id}/')

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_create(self) -> None:
        user = self.init_user()
        supplier = N(Supplier, user=user)
        api_client = self.authenticate_client(user)

        response = api_client.post(f"{self.endpoint}", model_to_dict(supplier))

        assert response.status_code == status.HTTP_201_CREATED

    def test_delete(self) -> None:
        user = self.init_user()
        supplier = self.init_supplier(user=user)
        api_client = self.authenticate_client(user)

        response = api_client.delete(f"{self.endpoint}{supplier.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update(self) -> None:
        user = self.init_user()
        supplier = self.init_supplier(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "name": "Test",
            "year_foundation": 2000,
            "country": "AF",
        }

        response = api_client.put(f"{self.endpoint}{supplier.id}/", new_data, format="json")

        data = json.loads(response.content)
        del data['buyer_amount']

        assert response.status_code == 200
        assert data == new_data

    def test_partial_update(self) -> None:
        user = self.init_user()
        supplier = self.init_supplier(user=user)
        api_client = self.authenticate_client(user)

        new_data = {
            "name": "Test",
            "year_foundation": 2000,
        }

        response = api_client.patch(f"{self.endpoint}{supplier.id}/", new_data, format="json")
        assert response.status_code == 200
