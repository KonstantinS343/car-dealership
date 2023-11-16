from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ActionCarDealership, ActionSupplier


class ActionCarDealershipAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Акция"), {"fields": ("name", "descritpion")}),
        (_("Скидка"), {"fields": ("discount",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
        (_("Даты"), {"fields": ("event_start", "event_end")}),
        (_("Зависомость"), {"fields": ("car_dealership", "car_model")}),
    )
    list_display = ("name", "descritpion", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "discount")
    ordering = ("name",)


class ActionSupplierAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Акция"), {"fields": ("name", "descritpion")}),
        (_("Скидка"), {"fields": ("discount",)}),
        (_("Активен"), {"fields": ("is_active",), }, ),
        (_("Даты"), {"fields": ("event_start", "event_end")}),
        (_("Зависомость"), {"fields": ("supplier", "car_model")}),
    )
    list_display = ("name", "descritpion", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "discount")
    ordering = ("name",)


admin.site.register(ActionCarDealership, ActionCarDealershipAdmin)
admin.site.register(ActionSupplier, ActionSupplierAdmin)
