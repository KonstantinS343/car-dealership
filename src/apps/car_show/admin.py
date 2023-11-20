from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import CarShow, CarShowModel, UniqueBuyersCarDealership, CarDealershipSuppliersList


class CarShowAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Описание"), {"fields": ("name", "country", "balance",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
        (
            _("Характеристики"), {
                "fields": (
                    "weight",
                    "engine_capacity",
                    "fuel_type",
                    "gearbox_type",
                    "car_body",
                )
            }
        ),
    )
    list_display = ("name", "country", "balance", "created_at", "update_at", "is_active")
    list_filter = ("name", "country", "is_active")
    search_fields = ("name", "country")
    ordering = ("name",)


class CarShowModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Автосалон"), {"fields": ("car_dealership",)}),
        (_("Модель автомобиля"), {"fields": ("car_model",)}),
        (_("Количество автомобилей"), {"fields": ("model_amount",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
    )
    list_display = ("car_dealership", "car_model", "model_amount", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("car_dealership", "car_model",)
    ordering = ("car_dealership",)


class UniqueBuyersCarDealershipAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Автосалон"), {"fields": ("car_dealership",)}),
        (_("Покупатель"), {"fields": ("buyer",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
    )
    list_display = ("car_dealership", "buyer", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("car_dealership", "buyer",)
    ordering = ("car_dealership",)


class CarDealershipSuppliersListAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Автосалон"), {"fields": ("car_dealership",)}),
        (_("Поставщик"), {"fields": ("supplier",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
    )
    list_display = ("car_dealership", "supplier", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("car_dealership", "supplier",)
    ordering = ("car_dealership",)


admin.site.register(UniqueBuyersCarDealership, UniqueBuyersCarDealershipAdmin)
admin.site.register(CarDealershipSuppliersList, CarDealershipSuppliersListAdmin)
admin.site.register(CarShowModel, CarShowModelAdmin)
admin.site.register(CarShow, CarShowAdmin)
