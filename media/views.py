import os
import uuid

from django.utils import timezone
from django.utils.text import slugify
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core import settings
from utils import messages, exceptions
from utils import debuger
from .models import Media
from .permissions import MediaIndexPermission, MediaCreatePermission, MediaShowPermission, MediaSoftDeletePermission, \
    MediaForceDeletePermission, \
    MediaRestorePermission
from .serializers import MediaCreateSerializer, MediaSerializer, MediaIndexSerializer
from webptools import cwebp


class MediaIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & MediaIndexPermission]

    def get(self, request):
        try:
            model = Media.objects.filter(user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            is_deleted = bool(request.GET.get('is_deleted', False))
            if is_deleted:
                model = model.filter(deleted_at__isnull=True)
            else:
                model = model.filter(deleted_at__isnull=False)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(MediaIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class MediaCreate(APIView):
    permission_classes = [IsAuthenticated & MediaCreatePermission]
    parser_classes = (MultiPartParser,)

    def post(self, request):
        try:
            serializer = MediaCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                file = request.FILES.get('file')
                # cwebp(input_image="python_logo.jpg", output_image="python_logo.webp",
                #       option="-q 80", logging="-v")
                name = uuid.uuid4().hex + '__' + slugify(os.path.splitext(file.name)[0]) + os.path.splitext(file.name)[
                    1]
                path = os.path.join(settings.MEDIA_ROOT, request.user.id, name)
                with open(path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                    destination.close()
                full_path = os.path.join(request.is_secure() and "https://" or "http://", request.get_host(),
                                         settings.MEDIA_URL + name)
                mime_type = file.content_type
                size = file.size / 1024
                created_at = timezone.now()
                result = Media.objects.create(path=path,
                                              full_path=full_path,
                                              mime_type=mime_type,
                                              size=size,
                                              created_at=created_at,
                                              user_id=request.user.id)
                return Response({
                    'message': messages.CREATED,
                    'data': MediaSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class MediaShow(APIView):
    permission_classes = [IsAuthenticated & MediaShowPermission]

    def get(self, request, pk):
        try:
            model = Media.objects.get(pk=pk)
            return Response(MediaSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class MediaSoftDelete(APIView):
    permission_classes = [IsAuthenticated & MediaSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Media.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class MediaForceDelete(APIView):
    permission_classes = [IsAuthenticated & MediaForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Media.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class MediaRestore(APIView):
    permission_classes = [IsAuthenticated & MediaRestorePermission]

    def put(self, request, pk):
        try:
            address = Media.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)
