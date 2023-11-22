from rest_framework import routers

from django.urls import include, path

from apps.car_show.api.views import CarShowViewSet, UniqueBuyersCarDealershipViewSet

router = routers.DefaultRouter()
router_unique_carshow = routers.DefaultRouter()
router.register(r'', CarShowViewSet, basename='carshow')
router_unique_carshow.register(r'', UniqueBuyersCarDealershipViewSet, basename='unique_buyers_carshow')

urlpatterns = [path('carshow/', include(router.urls)), path('carshow/unique/', include(router_unique_carshow.urls))]
