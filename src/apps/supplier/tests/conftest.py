import pytest

from ddf import G

from typing import Dict

from apps.supplier.model.models import Supplier


@pytest.fixture(scope='function')
def supplier(user, db) -> Supplier:
    supplier = G(Supplier, user=user)
    return supplier


@pytest.fixture(scope='class')
def supplier_update_data() -> Dict[str, str | int]:
    return {"name": "Test", "year_foundation": 2000, "country": "AF"}


@pytest.fixture(scope='class')
def supplier_partial_update_data() -> Dict[str, str | int]:
    return {
        "name": "Test",
        "year_foundation": 2000,
    }
