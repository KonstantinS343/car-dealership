import pytest

from ddf import G

from typing import Dict

from apps.buyer.model.models import Buyer
from apps.purchase_history.model.models import PurchasesSalesHistoryСarShow


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


@pytest.fixture(scope='function')
def buyer_history(db, buyer) -> PurchasesSalesHistoryСarShow:
    history = G(PurchasesSalesHistoryСarShow, buyer=buyer)
    return history
