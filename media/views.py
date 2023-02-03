from datetime import datetime

from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Media
from .permissions import MediaIndexPermission, MediaCreatePermission, MediaShowPermission, MediaSoftDeletePermission, MediaForceDeletePermission, \
    MediaRestorePermission
from .serializers import MediaCreateSerializer, MediaSerializer


class MediaIndex(APIView):
    permission_classes = [IsAuthenticated & MediaIndexPermission]

    def get(self, request):
        addresses = MediaSerializer(Media.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class MediaCreate(APIView):
    permission_classes = [IsAuthenticated & MediaCreatePermission]
    parser_classes = [FileUploadParser]
    def post(self, request):
        serializer = MediaCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MediaShow(APIView):
    permission_classes = [IsAuthenticated & MediaShowPermission]

    def get(self, request, pk):
        address = Media.objects.get(pk=pk)
        return Response(address)


class MediaSoftDelete(APIView):
    permission_classes = [IsAuthenticated & MediaSoftDeletePermission]

    def delete(self, request, pk):
        address = Media.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class MediaForceDelete(APIView):
    permission_classes = [IsAuthenticated & MediaForceDeletePermission]

    def delete(self, request, pk):
        address = Media.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class MediaRestore(APIView):
    permission_classes = [IsAuthenticated & MediaRestorePermission]

    def put(self, request, pk):
        address = Media.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
