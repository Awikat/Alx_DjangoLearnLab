from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to allow only authors of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Write permissions are only allowed to the author of the object
        return obj.author == request.user

