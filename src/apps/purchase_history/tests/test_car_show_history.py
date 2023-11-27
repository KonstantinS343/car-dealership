import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ddf import G

import json

from apps.common.models import User
from apps.purchase_history.models import PurchasesSalesHistoryСarShow
from apps.car_show.models import CarShow
from apps.buyer.models import Buyer


class TestPurchasesSalesHistoryСarShow:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/"
    USER_TYPE = 2

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
    def init_carshow(user) -> CarShow:
        carshow = G(CarShow, user=user)
        return carshow

    @staticmethod
    def init_buyer(user) -> CarShow:
        buyer = G(Buyer, user=user)
        return buyer

    @staticmethod
    def init_purchase_history(car_show=None, buyer=None) -> PurchasesSalesHistoryСarShow:
        if car_show:
            history = G(PurchasesSalesHistoryСarShow, car_dealership=car_show)
        elif buyer:
            history = G(PurchasesSalesHistoryСarShow, buyer=buyer)
        else:
            raise Exception("Аргументы!")
        return history

    def test_carshow_history_list(self) -> None:
        user = self.init_user()
        car_show = self.init_carshow(user=user)
        self.init_purchase_history(car_show=car_show)
        api_client = self.authenticate_client(user)

        response = api_client.get(self.endpoint + f'carshow/{car_show.id}/history/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    def test_buyer_history_list(self) -> None:
        user = self.init_user(type=1)
        buyer = self.init_buyer(user=user)
        self.init_purchase_history(buyer=buyer)
        api_client = self.authenticate_client(user)

        response = api_client.get(self.endpoint + f'carshow/{buyer.id}/buyer/history/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
