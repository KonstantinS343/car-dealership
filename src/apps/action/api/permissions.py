from rest_framework import permissions


class ActionCarDealershipPermission(permissions.BasePermission):
    """
    Класс разрешений, который даёт право на изменение модели ActionCarDealership
    только автосалону и админу.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.user_type == 2


class ActionSupplierPermission(permissions.BasePermission):
    """
    Класс разрешений, который даёт право на изменение модели ActionSupplier
    только поставщику и админу.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.user_type == 3
