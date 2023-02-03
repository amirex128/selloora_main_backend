from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .permissions import OrderIndexPermission, OrderCreatePermission, OrderShowPermission, OrderSoftDeletePermission, OrderForceDeletePermission, \
    OrderRestorePermission
from .serializers import OrderCreateSerializer, OrderSerializer


class OrderIndex(APIView):
    permission_classes = [IsAuthenticated & OrderIndexPermission]

    def get(self, request):
        addresses = OrderSerializer(Order.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class OrderCreate(APIView):
    permission_classes = [IsAuthenticated & OrderCreatePermission]

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class OrderShow(APIView):
    permission_classes = [IsAuthenticated & OrderShowPermission]

    def get(self, request, pk):
        address = Order.objects.get(pk=pk)
        return Response(address)


class OrderSoftDelete(APIView):
    permission_classes = [IsAuthenticated & OrderSoftDeletePermission]

    def delete(self, request, pk):
        address = Order.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class OrderForceDelete(APIView):
    permission_classes = [IsAuthenticated & OrderForceDeletePermission]

    def delete(self, request, pk):
        address = Order.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class OrderRestore(APIView):
    permission_classes = [IsAuthenticated & OrderRestorePermission]

    def put(self, request, pk):
        address = Order.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
