from rest_framework import permissions


class SupplierPermission(permissions.BasePermission):
    """
    Класс разрешений, который даёт право на взаимодействие с SupplierViewSet
    и UniqueBuyersSuppliersViewSet только админу, а также поставщику.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.user_type == 3
