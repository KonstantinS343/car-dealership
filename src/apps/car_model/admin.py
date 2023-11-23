from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Car


class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Класс"), {"fields": ("brand",)}),
        (
            _("Активен"),
            {
                "fields": ("is_active",),
            },
        ),
        (
            _("Характеристики"),
            {
                "fields": (
                    "weight",
                    "engine_capacity",
                    "fuel_type",
                    "gearbox_type",
                    "car_body",
                )
            },
        ),
    )
    list_display = ("brand", "car_body", "created_at", "update_at", "is_active")
    list_filter = ("is_active", "brand", "car_body", "fuel_type", "gearbox_type")
    search_fields = ("brand", "car_body")
    ordering = ("brand",)


admin.site.register(Car, CarAdmin)
