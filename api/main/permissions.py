from rest_framework import permissions
from django.utils.translation import gettext_lazy as _


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as an admin user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_superuser
        )


class OwnAccountOnly(permissions.BasePermission):
    message = _('Users can access or modify their own account only.')

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            obj == request.user
        )


class AnonymousUserOnly(permissions.BasePermission):
    message = _(
        "You cannot access this resource as it's only for unauthenticated "
        "users."
    )

    def has_permission(self, request, view):
        return request.user.is_authenticated is False


class IsSuperUserOrCanRegisterAndViewListOnly(permissions.BasePermission):
    # allow only superusers to access this resource
    # allow only anonymous users to register

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_superuser or
            (
                request.user.is_authenticated is False
                and
                (view.action == 'register' and request.method == 'POST')
            )
        )
