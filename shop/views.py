
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Shop
from .permissions import ShopIndexPermission, ShopCreatePermission, ShopShowPermission, \
    ShopUpdatePermission, ShopSoftDeletePermission, ShopForceDeletePermission, \
    ShopRestorePermission
from .serializers import ShopCreateSerializer, ShopUpdateSerializer, ShopSerializer, ShopIndexSerializer


class ShopIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ShopIndexPermission]

    def get(self, request):
        try:
            model = Shop.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ShopIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class ShopCreate(APIView):
    permission_classes = [IsAuthenticated & ShopCreatePermission]

    def post(self, request):
        try:
            serializer = ShopCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': ShopIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ShopShow(APIView):
    permission_classes = [IsAuthenticated & ShopShowPermission]

    def get(self, request, pk):
        try:
            model = Shop.objects.select_related('province', 'city').get(pk=pk)
            return Response(ShopSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ShopUpdate(APIView):
    permission_classes = [IsAuthenticated & ShopUpdatePermission]

    def put(self, request, pk):
        try:
            model = Shop.objects.get(pk=pk)
            serializer = ShopUpdateSerializer(model, data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.UPDATED,
                    'data': ShopIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class ShopSoftDelete(APIView):
    permission_classes = [IsAuthenticated & ShopSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Shop.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class ShopForceDelete(APIView):
    permission_classes = [IsAuthenticated & ShopForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Shop.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class ShopRestore(APIView):
    permission_classes = [IsAuthenticated & ShopRestorePermission]

    def put(self, request, pk):
        try:
            address = Shop.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

