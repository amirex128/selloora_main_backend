from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Shop
from .permissions import ShopIndexPermission, ShopCreatePermission, ShopShowPermission, \
    ShopUpdatePermission, ShopSoftDeletePermission, ShopForceDeletePermission, \
    ShopRestorePermission
from .serializers import ShopCreateSerializer, ShopUpdateSerializer, ShopSerializer


class ShopIndex(APIView):
    permission_classes = [IsAuthenticated & ShopIndexPermission]

    def get(self, request):
        addresses = ShopSerializer(Shop.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class ShopCreate(APIView):
    permission_classes = [IsAuthenticated & ShopCreatePermission]

    def post(self, request):
        serializer = ShopCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ShopShow(APIView):
    permission_classes = [IsAuthenticated & ShopShowPermission]

    def get(self, request, pk):
        address = Shop.objects.get(pk=pk)
        return Response(address)


class ShopUpdate(APIView):
    permission_classes = [IsAuthenticated & ShopUpdatePermission]

    def put(self, request, pk):
        address = Shop.objects.get(pk=pk)
        serializer = ShopUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ShopSoftDelete(APIView):
    permission_classes = [IsAuthenticated & ShopSoftDeletePermission]

    def delete(self, request, pk):
        address = Shop.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class ShopForceDelete(APIView):
    permission_classes = [IsAuthenticated & ShopForceDeletePermission]

    def delete(self, request, pk):
        address = Shop.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class ShopRestore(APIView):
    permission_classes = [IsAuthenticated & ShopRestorePermission]

    def put(self, request, pk):
        address = Shop.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
