import pytest

from ddf import G

from apps.purchase_history.model.models import PurchasesSalesHistoryСarShow, PurchasesSalesHistorySupplier


@pytest.fixture(scope='function')
def purchase_history_carshow(carshow, db) -> PurchasesSalesHistoryСarShow:
    history = G(PurchasesSalesHistoryСarShow, car_dealership=carshow)
    return history


@pytest.fixture(scope='function')
def purchase_history_buyer(buyer, db) -> PurchasesSalesHistoryСarShow:
    history = G(PurchasesSalesHistoryСarShow, buyer=buyer)
    return history


@pytest.fixture(scope='function')
def purchase_history_supplier(supplier, db) -> PurchasesSalesHistorySupplier:
    history = G(PurchasesSalesHistorySupplier, supplier=supplier)
    return history
