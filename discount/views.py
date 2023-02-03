from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Discount
from .permissions import DiscountIndexPermission, DiscountCreatePermission, DiscountShowPermission, \
    DiscountUpdatePermission, DiscountSoftDeletePermission, DiscountForceDeletePermission, \
    DiscountRestorePermission
from .serializers import DiscountCreateSerializer, DiscountUpdateSerializer, DiscountSerializer


class DiscountIndex(APIView):
    permission_classes = [IsAuthenticated & DiscountIndexPermission]

    def get(self, request):
        addresses = DiscountSerializer(Discount.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class DiscountCreate(APIView):
    permission_classes = [IsAuthenticated & DiscountCreatePermission]

    def post(self, request):
        serializer = DiscountCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DiscountShow(APIView):
    permission_classes = [IsAuthenticated & DiscountShowPermission]

    def get(self, request, pk):
        address = Discount.objects.get(pk=pk)
        return Response(address)


class DiscountUpdate(APIView):
    permission_classes = [IsAuthenticated & DiscountUpdatePermission]

    def put(self, request, pk):
        address = Discount.objects.get(pk=pk)
        serializer = DiscountUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DiscountSoftDelete(APIView):
    permission_classes = [IsAuthenticated & DiscountSoftDeletePermission]

    def delete(self, request, pk):
        address = Discount.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class DiscountForceDelete(APIView):
    permission_classes = [IsAuthenticated & DiscountForceDeletePermission]

    def delete(self, request, pk):
        address = Discount.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class DiscountRestore(APIView):
    permission_classes = [IsAuthenticated & DiscountRestorePermission]

    def put(self, request, pk):
        address = Discount.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
