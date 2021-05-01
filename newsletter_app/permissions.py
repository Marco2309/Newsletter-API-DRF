from rest_framework.permissions import BasePermission


class EditNewsletterPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        members = obj.members.all()
        admin = obj.user
        user = request.user
        if user == admin or user in members:
            return True
        return False
