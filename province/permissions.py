from .models import Province
from utils.base.permissions import BasePermission


class ProvinceIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True

