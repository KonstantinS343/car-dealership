from rest_framework import routers

from django.urls import include, path

from apps.supplier.api.views import SupplierViewSet, UniqueBuyersSuppliersViewSet

router = routers.DefaultRouter()
router_unique_suppliers = routers.DefaultRouter()
router.register(r'', SupplierViewSet, basename='supplier')
router_unique_suppliers.register(r'', UniqueBuyersSuppliersViewSet, basename='unique_buyers_supplier')

urlpatterns = [path('supplier/', include(router.urls)), path('supplier/unique/', include(router_unique_suppliers.urls))]
