from .models import Province
from utils.base.permissions import BasePermission


class ProvinceIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ProvinceCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ProvinceShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = Province.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProvinceUpdatePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = Province.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProvinceSoftDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = Province.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProvinceForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = Province.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProvinceRestorePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = Province.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True
