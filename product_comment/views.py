
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import ProductComment
from .permissions import ProductCommentIndexPermission, ProductCommentCreatePermission, ProductCommentShowPermission, ProductCommentSoftDeletePermission, ProductCommentForceDeletePermission, \
    ProductCommentRestorePermission
from .serializers import ProductCommentCreateSerializer, ProductCommentSerializer, ProductCommentIndexSerializer


class ProductCommentIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ProductCommentIndexPermission]

    def get(self, request):
        try:
            model = ProductComment.objects.filter(user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            is_deleted = bool(request.GET.get('is_deleted', False))
            if is_deleted:
                model = model.filter(deleted_at__isnull=True)
            else:
                model = model.filter(deleted_at__isnull=False)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ProductCommentIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ProductCommentCreate(APIView):
    permission_classes = [IsAuthenticated & ProductCommentCreatePermission]

    def post(self, request):
        try:
            serializer = ProductCommentCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': ProductCommentSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductCommentShow(APIView):
    permission_classes = [IsAuthenticated & ProductCommentShowPermission]

    def get(self, request, pk):
        try:
            model = ProductComment.objects.get(pk=pk)
            return Response(ProductCommentSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ProductCommentForceDelete(APIView):
    permission_classes = [IsAuthenticated & ProductCommentForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = ProductComment.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)
