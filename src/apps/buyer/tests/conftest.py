import pytest

from ddf import G

from typing import Dict

from apps.buyer.models import Buyer


@pytest.fixture(scope='function')
def buyer(user, db) -> Buyer:
    buyer = G(Buyer, user=user)
    return buyer


@pytest.fixture(scope='class')
def buyer_update_data() -> Dict[str, str | int]:
    return {
        "first_name": "TestName",
        "last_name": "TestLastName",
    }


@pytest.fixture(scope='class')
def buyer_partial_update_data() -> Dict[str, str | int]:
    return {
        "first_name": "TestName",
    }
