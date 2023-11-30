import pytest

from rest_framework import status

import json

from apps.common.conftest import api_client, user  # noqa
from apps.buyer.tests.conftest import buyer  # noqa
from apps.car_show.tests.conftest import carshow  # noqa


class TestPurchasesSalesHistoryСarShow:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/"

    @pytest.mark.parametrize('user_type', [2])
    def test_carshow_history_list(self, user_type, api_client, carshow, purchase_history_carshow) -> None:
        response = api_client.get(self.endpoint + f'carshow/{carshow.id}/history/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [1])
    def test_buyer_history_list(self, user_type, api_client, buyer, purchase_history_buyer) -> None:
        response = api_client.get(self.endpoint + f'carshow/{buyer.id}/buyer/history/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
