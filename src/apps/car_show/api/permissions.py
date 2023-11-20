from rest_framework import permissions


class CarShowPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            if request.user.is_superuser or request.user.user_type == 2:
                return True
        return False
