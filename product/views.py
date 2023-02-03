from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .permissions import ProductIndexPermission, ProductCreatePermission, ProductShowPermission, \
    ProductUpdatePermission, ProductSoftDeletePermission, ProductForceDeletePermission, \
    ProductRestorePermission
from .serializers import ProductCreateSerializer, ProductUpdateSerializer, ProductSerializer


class ProductIndex(APIView):
    permission_classes = [IsAuthenticated & ProductIndexPermission]

    def get(self, request):
        addresses = ProductSerializer(Product.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class ProductCreate(APIView):
    permission_classes = [IsAuthenticated & ProductCreatePermission]

    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductShow(APIView):
    permission_classes = [IsAuthenticated & ProductShowPermission]

    def get(self, request, pk):
        address = Product.objects.get(pk=pk)
        return Response(address)


class ProductUpdate(APIView):
    permission_classes = [IsAuthenticated & ProductUpdatePermission]

    def put(self, request, pk):
        address = Product.objects.get(pk=pk)
        serializer = ProductUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductSoftDelete(APIView):
    permission_classes = [IsAuthenticated & ProductSoftDeletePermission]

    def delete(self, request, pk):
        address = Product.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class ProductForceDelete(APIView):
    permission_classes = [IsAuthenticated & ProductForceDeletePermission]

    def delete(self, request, pk):
        address = Product.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class ProductRestore(APIView):
    permission_classes = [IsAuthenticated & ProductRestorePermission]

    def put(self, request, pk):
        address = Product.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
