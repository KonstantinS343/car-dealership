from rest_framework import routers

from django.urls import include, path

from apps.action.api.views import ActionCarDealershipViewSet, ActionSupplierViewSet

router_carshow = routers.DefaultRouter()
router_supplier = routers.DefaultRouter()
router_carshow.register(r'', ActionCarDealershipViewSet, basename='actions_carshow')
router_supplier.register(r'', ActionSupplierViewSet, basename='actions_supplier')

urlpatterns = [
    path('actions/carshow/', include(router_carshow.urls)),
    path('actions/supplier/', include(router_supplier.urls)),
]
