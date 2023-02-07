
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Product
from .permissions import ProductIndexPermission, ProductCreatePermission, ProductShowPermission, \
    ProductUpdatePermission, ProductSoftDeletePermission, ProductForceDeletePermission, \
    ProductRestorePermission
from .serializers import ProductCreateSerializer, ProductUpdateSerializer, ProductSerializer, ProductIndexSerializer


class ProductIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ProductIndexPermission]

    def get(self, request):
        try:
            model = Product.objects.filter(user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            is_deleted = bool(request.GET.get('is_deleted', False))
            if is_deleted:
                model = model.filter(deleted_at__isnull=True)
            else:
                model = model.filter(deleted_at__isnull=False)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ProductIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ProductCreate(APIView):
    permission_classes = [IsAuthenticated & ProductCreatePermission]

    def post(self, request):
        try:
            serializer = ProductCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': ProductSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductShow(APIView):
    permission_classes = [IsAuthenticated & ProductShowPermission]

    def get(self, request, pk):
        try:
            model = Product.objects.get(pk=pk)
            return Response(ProductSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductUpdate(APIView):
    permission_classes = [IsAuthenticated & ProductUpdatePermission]

    def put(self, request, pk):
        try:
            model = Product.objects.get(pk=pk)
            serializer = ProductUpdateSerializer(model, data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.UPDATED,
                    'data': ProductSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductSoftDelete(APIView):
    permission_classes = [IsAuthenticated & ProductSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Product.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductForceDelete(APIView):
    permission_classes = [IsAuthenticated & ProductForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Product.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class ProductRestore(APIView):
    permission_classes = [IsAuthenticated & ProductRestorePermission]

    def put(self, request, pk):
        try:
            address = Product.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

