from rest_framework import routers

from django.urls import include, path

from apps.supplier.api.views import SupplierViewSet

router = routers.DefaultRouter()
router.register(r'', SupplierViewSet, basename='supplier')

urlpatterns = [path('supplier/', include(router.urls))]
