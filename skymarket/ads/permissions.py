from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list' and (request.user.is_anonymous or request.user.is_authenticated):
            return True
        elif request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] and request.user.is_authenticated:
            return True
        return False


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'user':
            if request.method in ['GET', 'POST']:
                return True
            elif request.method in ['PUT', 'PATCH', 'DELETE'] and request.user == obj.author:
                return True
        return False
