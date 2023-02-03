from .models import City
from utils.base.permissions import BasePermission


class CityIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True
