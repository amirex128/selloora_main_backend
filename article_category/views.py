from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ArticleCategory
from .permissions import ArticleCategoryIndexPermission, ArticleCategoryCreatePermission, ArticleCategoryShowPermission, \
    ArticleCategoryUpdatePermission, ArticleCategorySoftDeletePermission, ArticleCategoryForceDeletePermission, \
    ArticleCategoryRestorePermission
from .serializers import ArticleCategoryCreateSerializer, ArticleCategoryUpdateSerializer, ArticleCategorySerializer


class ArticleCategoryIndex(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryIndexPermission]

    def get(self, request):
        addresses = ArticleCategorySerializer(ArticleCategory.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class ArticleCategoryCreate(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryCreatePermission]

    def post(self, request):
        serializer = ArticleCategoryCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleCategoryShow(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryShowPermission]

    def get(self, request, pk):
        address = ArticleCategory.objects.get(pk=pk)
        return Response(address)


class ArticleCategoryUpdate(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryUpdatePermission]

    def put(self, request, pk):
        address = ArticleCategory.objects.get(pk=pk)
        serializer = ArticleCategoryUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleCategorySoftDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleCategorySoftDeletePermission]

    def delete(self, request, pk):
        address = ArticleCategory.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class ArticleCategoryForceDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryForceDeletePermission]

    def delete(self, request, pk):
        address = ArticleCategory.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class ArticleCategoryRestore(APIView):
    permission_classes = [IsAuthenticated & ArticleCategoryRestorePermission]

    def put(self, request, pk):
        address = ArticleCategory.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
