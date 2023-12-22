import pytest

from ddf import G

from apps.purchase_history.model.models import PurchasesSalesHistoryСarShow, PurchasesSalesHistorySupplier
from apps.car_model.model.models import Car


@pytest.fixture(scope='function')
def purchase_history_carshow(carshow, db, model) -> PurchasesSalesHistoryСarShow:
    history = G(PurchasesSalesHistoryСarShow, car_dealership=carshow, car_model=G(Car, brand=model))
    return history


@pytest.fixture(scope='function')
def purchase_history_buyer(buyer, db, model) -> PurchasesSalesHistoryСarShow:
    history = G(PurchasesSalesHistoryСarShow, buyer=buyer, car_model=G(Car, brand=model))
    return history


@pytest.fixture(scope='function')
def purchase_history_supplier(supplier, db, model) -> PurchasesSalesHistorySupplier:
    history = G(PurchasesSalesHistorySupplier, supplier=supplier, car_model=G(Car, brand=model))
    return history
