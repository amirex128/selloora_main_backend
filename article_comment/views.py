
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import ArticleComment
from .permissions import ArticleCommentIndexPermission, ArticleCommentCreatePermission, ArticleCommentShowPermission, ArticleCommentForceDeletePermission
from .serializers import ArticleCommentCreateSerializer, ArticleCommentSerializer, ArticleCommentIndexSerializer


class ArticleCommentIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ArticleCommentIndexPermission]

    def get(self, request):
        try:
            model = ArticleComment.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ArticleCommentIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCommentCreate(APIView):
    permission_classes = [IsAuthenticated & ArticleCommentCreatePermission]

    def post(self, request):
        try:
            serializer = ArticleCommentCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': ArticleCommentIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ArticleCommentShow(APIView):
    permission_classes = [IsAuthenticated & ArticleCommentShowPermission]

    def get(self, request, pk):
        try:
            model = ArticleComment.objects.select_related('province', 'city').get(pk=pk)
            return Response(ArticleCommentSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ArticleCommentForceDelete(APIView):
    permission_classes = [IsAuthenticated & ArticleCommentForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = ArticleComment.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

