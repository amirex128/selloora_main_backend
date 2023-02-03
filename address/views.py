from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Address
from .permissions import AddressIndexPermission, AddressCreatePermission, AddressShowPermission, \
    AddressUpdatePermission, AddressSoftDeletePermission, AddressForceDeletePermission, \
    AddressRestorePermission
from .serializers import AddressCreateSerializer, AddressUpdateSerializer, AddressSerializer


class AddressIndex(APIView):
    permission_classes = [IsAuthenticated & AddressIndexPermission]

    def get(self, request):
        addresses = AddressSerializer(Address.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class AddressCreate(APIView):
    permission_classes = [IsAuthenticated & AddressCreatePermission]

    def post(self, request):
        serializer = AddressCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AddressShow(APIView):
    permission_classes = [IsAuthenticated & AddressShowPermission]

    def get(self, request, pk):
        address = Address.objects.get(pk=pk)
        return Response(address)


class AddressUpdate(APIView):
    permission_classes = [IsAuthenticated & AddressUpdatePermission]

    def put(self, request, pk):
        address = Address.objects.get(pk=pk)
        serializer = AddressUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AddressSoftDelete(APIView):
    permission_classes = [IsAuthenticated & AddressSoftDeletePermission]

    def delete(self, request, pk):
        address = Address.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class AddressForceDelete(APIView):
    permission_classes = [IsAuthenticated & AddressForceDeletePermission]

    def delete(self, request, pk):
        address = Address.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class AddressRestore(APIView):
    permission_classes = [IsAuthenticated & AddressRestorePermission]

    def put(self, request, pk):
        address = Address.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
