import pytest

from rest_framework import status

from ddf import G, N
from django.forms.models import model_to_dict

import json

from apps.supplier.model.models import Supplier, SupplierCarModel, UniqueBuyersSuppliers
from apps.car_model.models import Car
from apps.car_show.model.models import CarShow
from apps.common.conftest import api_client, user  # noqa


class TestSupplier:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/supplier/"
    AMOUNT_SUPPLIER_ATTRIBUTES = 4

    @pytest.mark.parametrize('user_type', [3])
    def test_list(self, user_type, api_client, supplier) -> None:
        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [3])
    def test_retrive(self, user_type, api_client, supplier) -> None:
        response = api_client.get(f'{self.endpoint}{supplier.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestSupplier.AMOUNT_SUPPLIER_ATTRIBUTES

    @pytest.mark.parametrize('user_type', [3])
    def test_create(self, user_type, api_client, user) -> None:
        supplier = N(Supplier, user=user)

        response = api_client.post(f"{self.endpoint}", model_to_dict(supplier))

        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.parametrize('user_type', [3])
    def test_delete(self, user_type, api_client, supplier) -> None:
        response = api_client.delete(f"{self.endpoint}{supplier.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.parametrize('user_type', [3])
    def test_update(self, user_type, api_client, supplier, supplier_update_data) -> None:
        response = api_client.put(f"{self.endpoint}{supplier.id}/", supplier_update_data, format="json")

        data = json.loads(response.content)
        del data['buyer_amount']

        assert response.status_code == status.HTTP_200_OK
        assert data == supplier_update_data

    @pytest.mark.parametrize('user_type', [3])
    def test_partial_update(self, user_type, api_client, supplier, supplier_partial_update_data) -> None:
        response = api_client.patch(f"{self.endpoint}{supplier.id}/", supplier_partial_update_data, format="json")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.parametrize('user_type', [3])
    def test_supplier_cars(self, user_type, api_client, supplier) -> None:
        response = api_client.get(f'{self.endpoint}{supplier.id}/cars/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

        G(SupplierCarModel, supplier=supplier, car_model=G(Car))

        response = api_client.get(f'{self.endpoint}{supplier.id}/cars/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [3])
    def test_supplier_unique_buyers(self, user_type, api_client, supplier) -> None:
        response = api_client.get(f'{self.endpoint}{supplier.id}/unique/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

        G(UniqueBuyersSuppliers, car_dealership=G(CarShow), supplier=supplier)

        response = api_client.get(f'{self.endpoint}{supplier.id}/unique/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
