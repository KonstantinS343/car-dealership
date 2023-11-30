import pytest

from ddf import G

from apps.car_model.models import Car


@pytest.fixture(scope='function')
def car() -> Car:
    car = G(Car)
    return car
