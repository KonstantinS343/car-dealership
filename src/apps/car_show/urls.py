from rest_framework import routers

from django.urls import include, path

from apps.car_show.api.views import CarShowViewSet

router = routers.DefaultRouter()
router.register(r'', CarShowViewSet, basename='carshow')

urlpatterns = [path('carshow/', include(router.urls))]
