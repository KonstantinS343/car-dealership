from rest_framework import routers

from django.urls import include, path

from apps.buyer.api.views import BuyerViewSet

router = routers.DefaultRouter()
router.register(r'', BuyerViewSet, basename='buyer')

urlpatterns = [path('buyer/', include(router.urls))]
