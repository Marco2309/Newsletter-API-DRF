from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class NotPermissions(BasePermission):

    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False
