import pytest

from rest_framework import status

from ddf import N
from django.forms.models import model_to_dict

import json

from apps.buyer.model.models import Buyer
from apps.common.conftest import api_client, user  # noqa


class TestBuyer:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/buyer/"
    AMOUNT_BUYER_ATTRIBUTES = 2

    @pytest.mark.parametrize('user_type', [1])
    def test_list(self, user_type, api_client, buyer) -> None:
        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [1])
    def test_retrive(self, user_type, api_client, buyer) -> None:
        response = api_client.get(f'{self.endpoint}{buyer.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestBuyer.AMOUNT_BUYER_ATTRIBUTES

    @pytest.mark.parametrize('user_type', [1])
    def test_create(self, user_type, api_client, user) -> None:
        buyer = N(Buyer, user=user)

        response = api_client.post(f"{self.endpoint}", model_to_dict(buyer))

        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.parametrize('user_type', [1])
    def test_delete(self, user_type, api_client, buyer) -> None:
        response = api_client.delete(f"{self.endpoint}{buyer.id}/")
        buyer = Buyer.objects.get(id=buyer.id)

        assert not buyer.is_active

        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.parametrize('user_type', [1])
    def test_update(self, user_type, api_client, buyer, buyer_update_data) -> None:
        response = api_client.put(f"{self.endpoint}{buyer.id}/", buyer_update_data, format="json")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.parametrize('user_type', [1])
    def test_partial_update(self, user_type, api_client, buyer, buyer_partial_update_data) -> None:
        response = api_client.patch(f"{self.endpoint}{buyer.id}/", buyer_partial_update_data, format="json")
        assert response.status_code == status.HTTP_200_OK
