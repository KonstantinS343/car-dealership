from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        'user_type',
        'update_at',
        'email_confirmed',
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    'user_type',
                    'email_confirmed',
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
