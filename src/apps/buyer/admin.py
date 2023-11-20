from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Buyer


class BuyerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('update_at',)


admin.site.register(Buyer, BuyerAdmin)
