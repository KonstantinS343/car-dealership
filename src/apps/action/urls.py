from rest_framework import routers

from django.urls import include, path

from apps.action.api.views import ActionCarDealershipViewSet

router = routers.DefaultRouter()
router.register(r'', ActionCarDealershipViewSet, basename='actions')

urlpatterns = [path('actions/', include(router.urls))]
