
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Assuming the Account model has an 'user' attribute.
        return obj.user == request.user
