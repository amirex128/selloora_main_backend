
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Domain
from .permissions import DomainIndexPermission, DomainCreatePermission, DomainShowPermission, DomainSoftDeletePermission, DomainForceDeletePermission, \
    DomainRestorePermission
from .serializers import DomainCreateSerializer, DomainSerializer, DomainIndexSerializer


class DomainIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & DomainIndexPermission]

    def get(self, request):
        try:
            model = Domain.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(DomainIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class DomainCreate(APIView):
    permission_classes = [IsAuthenticated & DomainCreatePermission]

    def post(self, request):
        try:
            serializer = DomainCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': DomainIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class DomainShow(APIView):
    permission_classes = [IsAuthenticated & DomainShowPermission]

    def get(self, request, pk):
        try:
            model = Domain.objects.select_related('province', 'city').get(pk=pk)
            return Response(DomainSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)



class DomainSoftDelete(APIView):
    permission_classes = [IsAuthenticated & DomainSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Domain.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class DomainForceDelete(APIView):
    permission_classes = [IsAuthenticated & DomainForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Domain.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class DomainRestore(APIView):
    permission_classes = [IsAuthenticated & DomainRestorePermission]

    def put(self, request, pk):
        try:
            address = Domain.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

