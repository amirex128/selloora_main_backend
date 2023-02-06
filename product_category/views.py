
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import ProductCategory
from .permissions import ProductCategoryIndexPermission, ProductCategoryCreatePermission, ProductCategoryShowPermission, \
    ProductCategoryUpdatePermission, ProductCategorySoftDeletePermission, ProductCategoryForceDeletePermission, \
    ProductCategoryRestorePermission
from .serializers import ProductCategoryCreateSerializer, ProductCategoryUpdateSerializer, ProductCategorySerializer, ProductCategoryIndexSerializer


class ProductCategoryIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ProductCategoryIndexPermission]

    def get(self, request):
        try:
            model = ProductCategory.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ProductCategoryIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ProductCategoryCreate(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryCreatePermission]

    def post(self, request):
        try:
            serializer = ProductCategoryCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': ProductCategoryIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductCategoryShow(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryShowPermission]

    def get(self, request, pk):
        try:
            model = ProductCategory.objects.select_related('province', 'city').get(pk=pk)
            return Response(ProductCategorySerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductCategoryUpdate(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryUpdatePermission]

    def put(self, request, pk):
        try:
            model = ProductCategory.objects.get(pk=pk)
            serializer = ProductCategoryUpdateSerializer(model, data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.UPDATED,
                    'data': ProductCategoryIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductCategorySoftDelete(APIView):
    permission_classes = [IsAuthenticated & ProductCategorySoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = ProductCategory.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductCategoryForceDelete(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = ProductCategory.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductCategoryRestore(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryRestorePermission]

    def put(self, request, pk):
        try:
            address = ProductCategory.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

