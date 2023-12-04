from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .model.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow


class PurchasesSalesHistorySupplierAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Поставщик"),
            {
                "fields": ("supplier",),
            },
        ),
        (
            _("Автосалон"),
            {
                "fields": ("car_dealership",),
            },
        ),
        (
            _("Автомобиль"),
            {
                "fields": ("car_model",),
            },
        ),
        (
            _("Права Доступа"),
            {
                "fields": ("is_active",),
            },
        ),
        (
            _("Активен"),
            {
                "fields": ("final_price",),
            },
        ),
    )
    list_display = ("supplier", "car_model", "car_dealership", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("supplier",)
    ordering = ("supplier",)


class PurchasesSalesHistoryСarShowAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Покупатель"),
            {
                "fields": ("buyer",),
            },
        ),
        (
            _("Автосалон"),
            {
                "fields": ("car_dealership",),
            },
        ),
        (
            _("Автомобиль"),
            {
                "fields": ("car_model",),
            },
        ),
        (
            _("Права Доступа"),
            {
                "fields": ("is_active",),
            },
        ),
        (
            _("Активен"),
            {
                "fields": ("final_price",),
            },
        ),
    )
    list_display = ("buyer", "car_dealership", "car_model", "created_at", "update_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("buyer",)
    ordering = ("buyer",)


admin.site.register(PurchasesSalesHistorySupplier, PurchasesSalesHistorySupplierAdmin)
admin.site.register(PurchasesSalesHistoryСarShow, PurchasesSalesHistoryСarShowAdmin)
