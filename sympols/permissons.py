from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            # allow all users to list user objects and create new user objects
            return True
        elif request.method in ['PUT', 'PATCH']:
            # allow authenticated staff users to update any user object
            return bool(request.user and request.user.is_authenticated and request.user.is_staff)
        elif request.method == 'DELETE':
            # allow staff and superusers to delete any user object
            return bool(request.user and request.user.is_superuser)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            # allow authenticated users to retrieve their own user object
            return bool(request.user and request.user.is_authenticated and obj == request.user)
        elif request.method in ['PUT', 'PATCH']:
            # allow authenticated staff users to update any user object
            return bool(request.user and request.user.is_authenticated and request.user.is_staff)
        elif request.method == 'DELETE':
            # allow staff and superusers to delete any user object
            return bool(request.user and request.user.is_staff)
        else:
            return False
