from .models import Order
from utils.base.permissions import BasePermission


class OrderIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class OrderCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class OrderShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Order.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class OrderSoftDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Order.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class OrderForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Order.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class OrderRestorePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Order.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True
