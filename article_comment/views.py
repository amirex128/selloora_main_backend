from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ArticleComment
from .permissions import ArticleCommentIndexPermission, ArticleCommentCreatePermission, ArticleCommentShowPermission,ArticleCommentForceDeletePermission
from .serializers import ArticleCommentCreateSerializer, ArticleCommentSerializer


class ArticleCommentIndex(APIView):
    permission_classes = [IsAuthenticated & ArticleCommentIndexPermission]

    def get(self, request):
        addresses = ArticleCommentSerializer(ArticleComment.objects.filter(), many=True)
        return Response(addresses)


class ArticleCommentCreate(APIView):
    permission_classes = [IsAuthenticated & ArticleCommentCreatePermission]

    def post(self, request):
        serializer = ArticleCommentCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleCommentShow(APIView):
    permission_classes = [IsAuthenticated & ArticleCommentShowPermission]

    def get(self, request, pk):
        address = ArticleComment.objects.get(pk=pk)
        return Response(address)


class ArticleCommentForceDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleCommentForceDeletePermission]

    def delete(self, request, pk):
        address = ArticleComment.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')
