from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import ArticleSerializer
from .models import Article


class ArticleIndex(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleCreate(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        # serializer['user_id'] = request.auth.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleShow(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleUpdate(APIView):
    def put(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleDelete(APIView):
    def delete(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response('Deleted')
