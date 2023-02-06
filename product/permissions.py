from .models import Product
from utils.base.permissions import BasePermission


class ProductIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ProductCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ProductShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Product.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProductUpdatePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Product.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProductSoftDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Product.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProductForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Product.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ProductRestorePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Product.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True
