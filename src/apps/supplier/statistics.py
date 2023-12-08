from django.db.models import Manager

from apps.purchase_history.model.models import PurchasesSalesHistorySupplier


def supplier_profit(supplier_id) -> Manager[PurchasesSalesHistorySupplier]:
    """
    Статистика для поставщика. Количество заработанных денег.
    """
    return PurchasesSalesHistorySupplier.objects.get_sales_profit(id=supplier_id)


def supplier_sold_cars_amount(supplier_id) -> Manager[PurchasesSalesHistorySupplier]:
    """
    Статистика для поставщика. Количество проданных автомобилей по моделям.
    """
    return PurchasesSalesHistorySupplier.objects.get_sold_cars_amount(id=supplier_id)


def supplier_sold_cars_profit(supplier_id) -> Manager[PurchasesSalesHistorySupplier]:
    """
    Статистика для поставщика. Количество заработанных денег с каждой модели.
    """
    return PurchasesSalesHistorySupplier.objects.get_sold_cars_profit(id=supplier_id)
