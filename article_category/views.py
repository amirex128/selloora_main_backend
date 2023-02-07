from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import ArticleCategory
from .permissions import ArticleCategoryIndexPermission, ArticleCategoryCreatePermission, ArticleCategoryShowPermission, \
    ArticleCategoryUpdatePermission, ArticleCategorySoftDeletePermission, ArticleCategoryForceDeletePermission, \
    ArticleCategoryRestorePermission
from .serializers import ArticleCategoryCreateSerializer, ArticleCategoryUpdateSerializer, ArticleCategorySerializer, \
    ArticleCategoryIndexSerializer, ArticleCategoryUpdateSortSerializer


class ArticleCategoryIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ArticleCategoryIndexPermission]

    def get(self, request):
        try:
            model = ArticleCategory.objects.filter(user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            is_deleted = bool(request.GET.get('is_deleted', False))
            if is_deleted:
                model = model.filter(deleted_at__isnull=True)
            else:
                model = model.filter(deleted_at__isnull=False)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ArticleCategoryIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCategoryCreate(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryCreatePermission]

    def post(self, request):
        try:
            serializer = ArticleCategoryCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': ArticleCategorySerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCategoryShow(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryShowPermission]

    def get(self, request, pk):
        try:
            model = ArticleCategory.objects.get(pk=pk)
            return Response(ArticleCategorySerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCategoryUpdate(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryUpdatePermission]

    def put(self, request, pk):
        try:
            model = ArticleCategory.objects.get(pk=pk)
            serializer = ArticleCategoryUpdateSerializer(model, data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.UPDATED,
                    'data': ArticleCategorySerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCategoryUpdateSort(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryIndexPermission]

    def put(self, request):
        try:
            serializer = ArticleCategoryUpdateSortSerializer(data=request.data)
            if serializer.is_valid():
                sorts = serializer.data.get('sorts')
                for sort in sorts:
                    article_category = ArticleCategory.objects.get(id=sort['id'])
                    article_category.sort = sort['sort']
                    article_category.save()
                return Response({
                    'message': messages.UPDATED,
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCategorySoftDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleCategorySoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = ArticleCategory.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCategoryForceDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = ArticleCategory.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCategoryRestore(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryRestorePermission]

    def put(self, request, pk):
        try:
            address = ArticleCategory.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)
