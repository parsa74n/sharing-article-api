from rest_framework import permissions




class IsOwnerPermission(permissions.BasePermission):
    """
    custom permission for users.
    if user is owner of object has this permission.
    """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False

    def has_permission(self, request, view):
        return super().has_permission(request, view)
