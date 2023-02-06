from .models import Media
from utils.base.permissions import BasePermission


class MediaIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class MediaCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class MediaShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Media.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class MediaSoftDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Media.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class MediaForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Media.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class MediaRestorePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Media.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True
