from .models import ArticleComment
from utils.base.permissions import BasePermission


class ArticleCommentIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ArticleCommentCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ArticleCommentShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = ArticleComment.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True

class ArticleCommentForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = ArticleComment.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


