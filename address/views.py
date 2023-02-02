from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Address
from .serializers import AddressSerializer


class AddressIndex(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)


class AddressCreate(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AddressShow(APIView):
    def get(self, request, pk):
        address = Address.objects.get(pk=pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)


class AddressUpdate(APIView):
    def put(self, request, pk):
        address = Address.objects.get(pk=pk)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AddressDelete(APIView):
    def delete(self, request, pk):
        address = Address.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')
