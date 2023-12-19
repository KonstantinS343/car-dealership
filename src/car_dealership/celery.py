import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_dealership.settings')

app = Celery('car_dealership')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'carshow-supplier-purchase-10-minute': {
        'task': 'apps.common.tasks.carshow_buy_car',
        'schedule': crontab(minute='*/10'),
    },
    'buyer-carshow-purchase-10-minute': {
        'task': 'apps.common.tasks.buyer_buy_car',
        'schedule': crontab(minute='*/10'),
    },
    'check-carshow-regular-supplier-list-1-hour': {
        'task': 'apps.common.tasks.check_supplier_list',
        'schedule': crontab(hour='*/1'),
    },
}
