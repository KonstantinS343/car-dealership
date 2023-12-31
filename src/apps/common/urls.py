from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.common.api.views import CustomUserViewSet

router = DefaultRouter()
router.register("users", CustomUserViewSet)

urlpatterns = [
    path("auth/", include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
