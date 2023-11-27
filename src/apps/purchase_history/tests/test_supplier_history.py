import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ddf import G

import json

from apps.common.models import User
from apps.purchase_history.models import PurchasesSalesHistorySupplier
from apps.supplier.models import Supplier


class TestPurchasesSalesHistorySupplier:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/"
    USER_TYPE = 3

    @staticmethod
    def authenticate_client(user) -> APIClient:
        refresh = RefreshToken.for_user(user)
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        return api_client

    @staticmethod
    def init_user(type=USER_TYPE) -> User:
        user = G(User, user_type=type)
        return user

    @staticmethod
    def init_supplier(user) -> Supplier:
        supplier = G(Supplier, user=user)
        return supplier

    @staticmethod
    def init_purchase_history(supplier) -> PurchasesSalesHistorySupplier:
        history = G(PurchasesSalesHistorySupplier, supplier=supplier)
        return history

    def test_supplier_history_list(self) -> None:
        user = self.init_user()
        supplier = self.init_supplier(user=user)
        self.init_purchase_history(supplier=supplier)
        api_client = self.authenticate_client(user)
        print(PurchasesSalesHistorySupplier.objects.filter(is_active=True, supplier=supplier))

        response = api_client.get(self.endpoint + f'supplier/{supplier.id}/history/')
        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
