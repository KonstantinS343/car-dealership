import pytest

from ddf import G

from apps.car_model.model.models import Car


@pytest.fixture(scope='function')
def car(db, weight) -> Car:
    car = G(Car, weight=weight)
    return car
