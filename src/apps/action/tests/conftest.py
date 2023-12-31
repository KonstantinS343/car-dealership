import pytest

from ddf import G

from typing import Dict

from apps.action.model.models import ActionCarDealership, ActionSupplier
from apps.car_show.model.models import CarShow
from apps.supplier.model.models import Supplier
from apps.car_model.model.models import Car


@pytest.fixture(scope='function')
def carshow_action(user, model) -> ActionCarDealership:
    carshow_action = G(ActionCarDealership, car_dealership=G(CarShow, user=user), car_model=G(Car, brand=model))
    return carshow_action


@pytest.fixture(scope='function')
def supplier_action(user, model) -> ActionSupplier:
    supplier_action = G(ActionSupplier, supplier=G(Supplier, user=user), car_model=G(Car, brand=model))
    return supplier_action


@pytest.fixture(scope='class')
def action_update_data() -> Dict[str, str | float]:
    return {
        "name": "Test",
        "descritpion": "Test",
        "event_start": "2023-11-11",
        "event_end": "2023-12-12",
        "discount": 0.3,
    }


@pytest.fixture(scope='class')
def action_partial_update_data() -> Dict[str, str | float]:
    return {
        "name": "Test",
        "discount": 0.3,
    }
