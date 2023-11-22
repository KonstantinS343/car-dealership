from rest_framework import permissions


class PurchasesSalesHistoryСarShowPermission(permissions.BasePermission):
    """
    Класс разрешений, который даёт право на просмотр модели PurchasesSalesHistoryСarShow только админу,
    а также автосалону и покупателю.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.user_type == 2 or request.user.user_type == 1:
            return True
        return False


class PurchasesSalesHistorySupplierPermission(permissions.BasePermission):
    """
    Класс разрешений, который даёт право на просмотр модели PurchasesSalesHistorySupplier только админу,
    а также автосалону и поставщику.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.user_type == 2 or request.user.user_type == 3:
            return True
        return False
