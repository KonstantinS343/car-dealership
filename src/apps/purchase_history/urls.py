from rest_framework import routers

from django.urls import include, path

from apps.purchase_history.api.views import PurchasesSalesHistorySupplierViewSet, PurchasesSalesHistoryСarShowViewSet

router_carshow = routers.DefaultRouter()
router_supplier = routers.DefaultRouter()
router_carshow.register(r'', PurchasesSalesHistoryСarShowViewSet, basename='history_carshow')
router_supplier.register(r'', PurchasesSalesHistorySupplierViewSet, basename='history_supplier')

urlpatterns = [path('history/carshow/', include(router_carshow.urls)), path('history/supplier/', include(router_supplier.urls))]
