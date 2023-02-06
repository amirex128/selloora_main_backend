from .models import Ticket
from utils.base.permissions import BasePermission


class TicketIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class TicketCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class TicketShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Ticket.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True

class TicketSoftDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Ticket.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class TicketForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Ticket.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class TicketRestorePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Ticket.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True
