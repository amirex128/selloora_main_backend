from .models import Article
from utils.base.permissions import BasePermission


class ArticleIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ArticleCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ArticleShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Article.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleUpdatePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Article.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleSoftDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Article.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Article.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleRestorePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('pk')
        model = Article.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True
