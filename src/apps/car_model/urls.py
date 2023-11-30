from rest_framework import routers

from django.urls import include, path

from apps.car_model.api.views import CarViewSet

router = routers.DefaultRouter()
router.register(r'', CarViewSet, basename='carmodels')

urlpatterns = [path('carmodels/', include(router.urls))]
