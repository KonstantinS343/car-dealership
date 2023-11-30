import pytest

from ddf import G

from typing import Dict

from apps.car_show.models import CarShow


@pytest.fixture(scope='function')
def carshow(user, db) -> CarShow:
    carshow = G(CarShow, user=user)
    return carshow


@pytest.fixture(scope='class')
def carshow_update_data() -> Dict[str, str | float]:
    return {
        "name": "Test",
        "country": "AF",
        "weight": 1.2,
        "engine_capacity": 2.3,
        "fuel_type": "Diesel",
        "gearbox_type": "Automatic",
        "car_body": "Sedan",
    }


@pytest.fixture(scope='class')
def carshow_partial_update_data() -> Dict[str, str]:
    return {
        "name": "Test",
        "car_body": 'Sedan',
    }
