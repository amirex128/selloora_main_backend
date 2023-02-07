from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Article
from .permissions import ArticleIndexPermission, ArticleCreatePermission, ArticleShowPermission, \
    ArticleUpdatePermission, ArticleSoftDeletePermission, ArticleForceDeletePermission, \
    ArticleRestorePermission
from .serializers import ArticleCreateSerializer, ArticleUpdateSerializer, ArticleSerializer, ArticleIndexSerializer


class ArticleIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ArticleIndexPermission]

    def get(self, request):
        try:
            model = Article.objects.filter(user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            is_deleted = bool(request.GET.get('is_deleted', False))
            if is_deleted:
                model = model.filter(deleted_at__isnull=True)
            else:
                model = model.filter(deleted_at__isnull=False)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ArticleIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCreate(APIView):
    permission_classes = [IsAuthenticated & ArticleCreatePermission]

    def post(self, request):
        try:
            serializer = ArticleCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': ArticleSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleShow(APIView):
    permission_classes = [IsAuthenticated & ArticleShowPermission]

    def get(self, request, pk):
        try:
            model = Article.objects.select_related('media').get(pk=pk)
            return Response(ArticleSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleUpdate(APIView):
    permission_classes = [IsAuthenticated & ArticleUpdatePermission]

    def put(self, request, pk):
        try:
            model = Article.objects.get(pk=pk)
            serializer = ArticleUpdateSerializer(model, data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.UPDATED,
                    'data': ArticleSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleSoftDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Article.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleForceDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Article.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleRestore(APIView):
    permission_classes = [IsAuthenticated & ArticleRestorePermission]

    def put(self, request, pk):
        try:
            address = Article.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)
