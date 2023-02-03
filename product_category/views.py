from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductCategory
from .permissions import ProductCategoryIndexPermission, ProductCategoryCreatePermission, ProductCategoryShowPermission, \
    ProductCategoryUpdatePermission, ProductCategorySoftDeletePermission, ProductCategoryForceDeletePermission, \
    ProductCategoryRestorePermission
from .serializers import ProductCategoryCreateSerializer, ProductCategoryUpdateSerializer, ProductCategorySerializer


class ProductCategoryIndex(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryIndexPermission]

    def get(self, request):
        addresses = ProductCategorySerializer(ProductCategory.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class ProductCategoryCreate(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryCreatePermission]

    def post(self, request):
        serializer = ProductCategoryCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductCategoryShow(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryShowPermission]

    def get(self, request, pk):
        address = ProductCategory.objects.get(pk=pk)
        return Response(address)


class ProductCategoryUpdate(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryUpdatePermission]

    def put(self, request, pk):
        address = ProductCategory.objects.get(pk=pk)
        serializer = ProductCategoryUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductCategorySoftDelete(APIView):
    permission_classes = [IsAuthenticated & ProductCategorySoftDeletePermission]

    def delete(self, request, pk):
        address = ProductCategory.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class ProductCategoryForceDelete(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryForceDeletePermission]

    def delete(self, request, pk):
        address = ProductCategory.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class ProductCategoryRestore(APIView):
    permission_classes = [IsAuthenticated & ProductCategoryRestorePermission]

    def put(self, request, pk):
        address = ProductCategory.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
