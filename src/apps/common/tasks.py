from celery import shared_task

from apps.car_show.model.models import CarShow

# from apps.car_model.model.models import Car
from apps.purchase_history.model.models import PurchasesSalesHistoryСarShow


@shared_task
def buy_car():
    shops = CarShow.objects.get_all_active_carshow()
    most_popular_car = PurchasesSalesHistoryСarShow.objects.get_popular_car_brand()

    for shop in shops.iterator():
        print(type(most_popular_car))
