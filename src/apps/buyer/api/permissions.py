from rest_framework import permissions


class BuyerPermission(permissions.BasePermission):
    """
    Класс разрешений, который даёт право на взаимодействие с BuyerViewSet только админу,
    а также клиенту.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.user_type == 1
