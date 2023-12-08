from django.db.models import Manager

from apps.purchase_history.model.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow


def profit(id, type) -> Manager[PurchasesSalesHistorySupplier | PurchasesSalesHistoryСarShow]:
    """
    Статистика для поставщика, покупателя, автосалона. Количество заработанных/потраченных денег.
    """
    if type == 'supplier':
        queryset = PurchasesSalesHistorySupplier.objects.supplier_history(id=id)
        return PurchasesSalesHistorySupplier.objects.get_sales(queryset)
    elif type == 'carshow':
        queryset = PurchasesSalesHistoryСarShow.objects.car_show_history(id=id)
        return PurchasesSalesHistoryСarShow.objects.get_sales(queryset)

    queryset = PurchasesSalesHistoryСarShow.objects.buyer_history(id=id)
    return PurchasesSalesHistoryСarShow.objects.get_sales(queryset)


def cars_amount(id, type) -> Manager[PurchasesSalesHistorySupplier | PurchasesSalesHistoryСarShow]:
    """
    Статистика для поставщика, покупателя, автосалона. Количество проданных/потраченных автомобилей по моделям.
    """
    if type == 'supplier':
        queryset = PurchasesSalesHistorySupplier.objects.supplier_history(id=id)
        return PurchasesSalesHistorySupplier.objects.get_cars_amount(queryset)
    elif type == 'carshow':
        queryset = PurchasesSalesHistoryСarShow.objects.car_show_history(id=id)
        return PurchasesSalesHistoryСarShow.objects.get_cars_amount(queryset)

    queryset = PurchasesSalesHistoryСarShow.objects.buyer_history(id=id)
    return PurchasesSalesHistoryСarShow.objects.get_cars_amount(queryset)


def cars_money_sale(id, type) -> Manager[PurchasesSalesHistorySupplier | PurchasesSalesHistoryСarShow]:
    """
    Статистика для поставщика, покупателя, автосалона. Количество заработанных/потраченных денег по каждой модели.
    """
    if type == 'supplier':
        queryset = PurchasesSalesHistorySupplier.objects.supplier_history(id=id)
        return PurchasesSalesHistorySupplier.objects.get_cars(queryset)
    elif type == 'carshow':
        queryset = PurchasesSalesHistoryСarShow.objects.car_show_history(id=id)
        return PurchasesSalesHistoryСarShow.objects.get_cars(queryset)

    queryset = PurchasesSalesHistoryСarShow.objects.buyer_history(id=id)
    return PurchasesSalesHistoryСarShow.objects.get_cars(queryset)
