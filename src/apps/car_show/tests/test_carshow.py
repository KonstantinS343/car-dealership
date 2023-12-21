import pytest

from rest_framework import status

from ddf import G, N
from django.forms.models import model_to_dict

import json

from apps.supplier.model.models import Supplier
from apps.car_model.model.models import Car
from apps.car_show.model.models import CarShow, CarShowModel, UniqueBuyersCarDealership, CarDealershipSuppliersList
from apps.buyer.model.models import Buyer

from apps.common.conftest import api_client, user  # noqa


class TestCarShow:
    pytestmark = pytest.mark.django_db
    endpoint = "/api/v1/carshow/"
    AMOUNT_CARSHOW_ATTRIBUTES = 8

    @pytest.mark.parametrize('user_type', [2])
    def test_list(self, user_type, api_client, carshow) -> None:
        response = api_client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [2])
    def test_retrive(self, user_type, api_client, carshow) -> None:
        response = api_client.get(f'{self.endpoint}{carshow.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == TestCarShow.AMOUNT_CARSHOW_ATTRIBUTES

    @pytest.mark.parametrize('user_type', [2])
    def test_create(self, user_type, api_client, user) -> None:
        carshow = N(CarShow, user=user, engine_capacity=2.0, weight=1.23)

        response = api_client.post(f"{self.endpoint}", model_to_dict(carshow))

        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.parametrize('user_type', [2])
    def test_delete(self, user_type, api_client, carshow) -> None:
        response = api_client.delete(f"{self.endpoint}{carshow.id}/")
        carshow = CarShow.objects.get(id=carshow.id)

        assert not carshow.is_active

        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.parametrize('user_type', [2])
    def test_update(self, user_type, api_client, carshow, carshow_update_data) -> None:
        response = api_client.put(f"{self.endpoint}{carshow.id}/", carshow_update_data, format="json")

        data = json.loads(response.content)
        del data['balance']

        assert response.status_code == status.HTTP_200_OK
        assert data == carshow_update_data

    @pytest.mark.parametrize('user_type', [2])
    def test_partial_update(self, user_type, api_client, carshow, carshow_partial_update_data) -> None:
        response = api_client.patch(f"{self.endpoint}{carshow.id}/", carshow_partial_update_data, format="json")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.parametrize('user_type', [2])
    def test_supplier_cars(self, user_type, api_client, carshow) -> None:
        response = api_client.get(f'{self.endpoint}{carshow.id}/cars/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

        G(CarShowModel, car_dealership=carshow, car_model=G(Car))

        response = api_client.get(f'{self.endpoint}{carshow.id}/cars/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [2])
    def test_supplier_unique_buyers(self, user_type, api_client, carshow) -> None:
        response = api_client.get(f'{self.endpoint}{carshow.id}/unique/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

        G(UniqueBuyersCarDealership, car_dealership=carshow, buyer=G(Buyer))

        response = api_client.get(f'{self.endpoint}{carshow.id}/unique/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1

    @pytest.mark.parametrize('user_type', [2])
    def test_list_carshow_suppliers(self, user_type, api_client, carshow) -> None:
        response = api_client.get(f'{self.endpoint}{carshow.id}/suppliers/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

        G(CarDealershipSuppliersList, car_dealership=carshow, supplier=G(Supplier))

        response = api_client.get(f'{self.endpoint}{carshow.id}/suppliers/')

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 1
