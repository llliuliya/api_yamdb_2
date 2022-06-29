from rest_framework import permissions


class Admin(permissions.BasePermission):
    """Права доступа для админа."""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'admin'
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.role == 'admin'
        return False


class User(permissions.BasePermission):
    """Права доступа для аутентифицированных пользователей."""
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class ReadOnly(permissions.BasePermission):
    """Права доступа для анонимов."""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class Superuser(permissions.BasePermission):
    """Права доступа для суперюзера."""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.is_superuser
        return False


class Moderator(permissions.BasePermission):
    """Права доступа для модератора."""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'moderator'
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.role == 'moderator'
        return False
