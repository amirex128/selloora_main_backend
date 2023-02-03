from .models import ArticleCategory
from utils.base.permissions import BasePermission


class ArticleCategoryIndexPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ArticleCategoryCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class ArticleCategoryShowPermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = ArticleCategory.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleCategoryUpdatePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = ArticleCategory.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleCategorySoftDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = ArticleCategory.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleCategoryForceDeletePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = ArticleCategory.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True


class ArticleCategoryRestorePermission(BasePermission):
    def has_permission(self, request, view):
        pk = request.resolver_match.kwargs.get('id')
        model = ArticleCategory.objects.filter(id=pk).first()
        if model is None:
            return False
        if model.user_id != request.user.id:
            return False
        return True
