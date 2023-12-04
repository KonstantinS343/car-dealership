import pytest

from rest_framework import status

from ddf import G, N
from django.forms.models import model_to_dict

import json

from apps.supplier.model.models import Supplier
from apps.action.models import ActionSupplier
from apps.common.conftest import api_client, user  # noqa


class TestActionSupplier:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/actions/supplier/"
    AMOUNT_ACTION_ATTRIBUTES = 7

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_list(self, user_type, api_client, supplier_action) -> None:
        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_retrive(self, user_type, api_client, supplier_action) -> None:
        response = api_client.get(f'{self.endpoint}{supplier_action.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestActionSupplier.AMOUNT_ACTION_ATTRIBUTES

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_create(self, user_type, api_client, supplier_action) -> None:
        supplier = G(Supplier)
        action = N(ActionSupplier, supplier=supplier, discount=0.4)

        response = api_client.post(f"{self.endpoint}", model_to_dict(action))

        if user_type == 3:
            assert response.status_code == status.HTTP_201_CREATED
        else:
            assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_delete(self, user_type, api_client, supplier_action) -> None:
        response = api_client.delete(f"{self.endpoint}{supplier_action.id}/")

        if user_type == 3:
            assert response.status_code == status.HTTP_204_NO_CONTENT
        else:
            assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_update(self, user_type, api_client, supplier_action, action_update_data) -> None:
        response = api_client.put(f"{self.endpoint}{supplier_action.id}/", action_update_data, format="json")

        if user_type == 3:
            assert response.status_code == status.HTTP_200_OK
        else:
            assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize('user_type', [1, 2, 3])
    def test_partial_update(self, user_type, api_client, supplier_action, action_partial_update_data) -> None:
        response = api_client.patch(f"{self.endpoint}{supplier_action.id}/", action_partial_update_data, format="json")

        if user_type == 3:
            assert response.status_code == status.HTTP_200_OK
        else:
            assert response.status_code == status.HTTP_403_FORBIDDEN
