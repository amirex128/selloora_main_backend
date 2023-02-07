from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Address
from .permissions import AddressIndexPermission, AddressCreatePermission, AddressShowPermission, \
    AddressUpdatePermission, AddressSoftDeletePermission, AddressForceDeletePermission, \
    AddressRestorePermission
from .serializers import AddressCreateSerializer, AddressUpdateSerializer, AddressSerializer, AddressIndexSerializer


class AddressIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & AddressIndexPermission]

    def get(self, request):
        try:
            model = Address.objects.filter(deleted_at__isnull=True, user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(AddressIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class AddressCreate(APIView):
    permission_classes = [IsAuthenticated & AddressCreatePermission]

    def post(self, request):
        try:
            serializer = AddressCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': AddressSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class AddressShow(APIView):
    permission_classes = [IsAuthenticated & AddressShowPermission]

    def get(self, request, pk):
        try:
            model = Address.objects.get(pk=pk)
            return Response(AddressSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class AddressUpdate(APIView):
    permission_classes = [IsAuthenticated & AddressUpdatePermission]

    def put(self, request, pk):
        try:
            model = Address.objects.get(pk=pk)
            serializer = AddressUpdateSerializer(model, data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.UPDATED,
                    'data': AddressSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)


class AddressSoftDelete(APIView):
    permission_classes = [IsAuthenticated & AddressSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Address.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class AddressForceDelete(APIView):
    permission_classes = [IsAuthenticated & AddressForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)


class AddressRestore(APIView):
    permission_classes = [IsAuthenticated & AddressRestorePermission]

    def put(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

