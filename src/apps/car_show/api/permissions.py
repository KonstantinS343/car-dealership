from rest_framework import permissions


class CarShowPermission(permissions.BasePermission):
    """
    Класс разрешений, который даёт право на взаимодействие с CarShowViewSet
    и UniqueBuyersCarDealership только админу, а также пользователю связанному с автосалоном.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.user_type == 2:
            return True
        return False
