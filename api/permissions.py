from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, object):
        """check if user has the permission to do that"""
        if request.method in permissions.SAFE_METHODS: #is it in safe methods? Like GET?
            return True
        else:
            return object.id == request.user.id #in case user tries to access/edit sensitive data, returns true if those data are his own data, so np
