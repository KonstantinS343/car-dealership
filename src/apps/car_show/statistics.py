from django.db.models import Manager

from apps.purchase_history.model.models import PurchasesSalesHistoryСarShow


def carshow_profit(supplier_id) -> Manager[PurchasesSalesHistoryСarShow]:
    """
    Статистика для автосалона. Количество заработанных денег.
    """
    return PurchasesSalesHistoryСarShow.objects.get_sales_profit(id=supplier_id)


def carshow_sold_cars_amount(supplier_id) -> Manager[PurchasesSalesHistoryСarShow]:
    """
    Статистика для автосалона. Количество проданных автомобилей по моделям.
    """
    return PurchasesSalesHistoryСarShow.objects.get_sold_cars_amount(id=supplier_id)


def carshow_sold_cars_profit(supplier_id) -> Manager[PurchasesSalesHistoryСarShow]:
    """
    Статистика для автосалона. Количество заработанных денег с каждой модели.
    """
    return PurchasesSalesHistoryСarShow.objects.get_sold_cars_profit(id=supplier_id)
