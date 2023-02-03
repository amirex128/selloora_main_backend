from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Domain
from .permissions import DomainIndexPermission, DomainCreatePermission, DomainShowPermission, DomainSoftDeletePermission, DomainForceDeletePermission, \
    DomainRestorePermission
from .serializers import DomainCreateSerializer, DomainSerializer


class DomainIndex(APIView):
    permission_classes = [IsAuthenticated & DomainIndexPermission]

    def get(self, request):
        addresses = DomainSerializer(Domain.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class DomainCreate(APIView):
    permission_classes = [IsAuthenticated & DomainCreatePermission]

    def post(self, request):
        serializer = DomainCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DomainShow(APIView):
    permission_classes = [IsAuthenticated & DomainShowPermission]

    def get(self, request, pk):
        address = Domain.objects.get(pk=pk)
        return Response(address)


class DomainSoftDelete(APIView):
    permission_classes = [IsAuthenticated & DomainSoftDeletePermission]

    def delete(self, request, pk):
        address = Domain.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class DomainForceDelete(APIView):
    permission_classes = [IsAuthenticated & DomainForceDeletePermission]

    def delete(self, request, pk):
        address = Domain.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class DomainRestore(APIView):
    permission_classes = [IsAuthenticated & DomainRestorePermission]

    def put(self, request, pk):
        address = Domain.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
