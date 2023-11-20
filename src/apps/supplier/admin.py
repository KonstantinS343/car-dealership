from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Supplier, SupplierCarModel, UniqueBuyersSuppliers


class SupplierAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Описание"), {"fields": ("name", "country", "year_foundation", "buyer_amount")}),
        (_("Активен"), {"fields": ("is_active",), }, ),
    )
    list_display = ("name", "country", "year_foundation", "buyer_amount", "created_at", "update_at", "is_active")
    list_filter = ("name", "country", "is_active")
    search_fields = ("name", "country")
    ordering = ("name", "buyer_amount")


class SupplierCarModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Поставщик"), {"fields": ("supplier",)}),
        (_("Модель автомобиля"), {"fields": ("car_model",)}),
        (_("Цена"), {"fields": ("price",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
    )
    list_display = ("supplier", "car_model", "price", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("supplier", "car_model",)
    ordering = ("supplier", "price")


class UniqueBuyersSuppliersAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Автосалон"), {"fields": ("car_dealership",)}),
        (_("Поставщик"), {"fields": ("supplier",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
    )
    list_display = ("car_dealership", "supplier", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("car_dealership", "supplier",)
    ordering = ("car_dealership",)


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierCarModel, SupplierCarModelAdmin)
admin.site.register(UniqueBuyersSuppliers, UniqueBuyersSuppliersAdmin)
