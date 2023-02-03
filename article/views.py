from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .permissions import ArticleIndexPermission, ArticleCreatePermission, ArticleShowPermission, \
    ArticleUpdatePermission, ArticleSoftDeletePermission, ArticleForceDeletePermission, \
    ArticleRestorePermission
from .serializers import ArticleCreateSerializer, ArticleUpdateSerializer, ArticleSerializer


class ArticleIndex(APIView):
    permission_classes = [IsAuthenticated & ArticleIndexPermission]

    def get(self, request):
        addresses = ArticleSerializer(Article.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class ArticleCreate(APIView):
    permission_classes = [IsAuthenticated & ArticleCreatePermission]

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleShow(APIView):
    permission_classes = [IsAuthenticated & ArticleShowPermission]

    def get(self, request, pk):
        address = Article.objects.get(pk=pk)
        return Response(address)


class ArticleUpdate(APIView):
    permission_classes = [IsAuthenticated & ArticleUpdatePermission]

    def put(self, request, pk):
        address = Article.objects.get(pk=pk)
        serializer = ArticleUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleSoftDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleSoftDeletePermission]

    def delete(self, request, pk):
        address = Article.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class ArticleForceDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleForceDeletePermission]

    def delete(self, request, pk):
        address = Article.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class ArticleRestore(APIView):
    permission_classes = [IsAuthenticated & ArticleRestorePermission]

    def put(self, request, pk):
        address = Article.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
