"""
URL configuration for car_dealership project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .swagger import urlpatterns as docs_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.action.urls')),
    path('api/v1/', include('apps.car_show.urls')),
    path('api/v1/', include('apps.car_model.urls')),
    path('api/v1/', include('apps.supplier.urls')),
    path('api/v1/', include('apps.buyer.urls')),
    path('api/v1/', include('apps.action.urls')),
    path('api/v1/', include('apps.purchase_history.urls')),
    path('api/v1/', include('apps.common.urls')),
] + docs_url


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
