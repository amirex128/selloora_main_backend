
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Order
from .permissions import OrderIndexPermission, OrderCreatePermission, OrderShowPermission, OrderSoftDeletePermission, OrderForceDeletePermission, \
    OrderRestorePermission
from .serializers import OrderCreateSerializer, OrderSerializer, OrderIndexSerializer


class OrderIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & OrderIndexPermission]

    def get(self, request):
        try:
            model = Order.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(OrderIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class OrderCreate(APIView):
    permission_classes = [IsAuthenticated & OrderCreatePermission]

    def post(self, request):
        try:
            serializer = OrderCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': OrderSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class OrderShow(APIView):
    permission_classes = [IsAuthenticated & OrderShowPermission]

    def get(self, request, pk):
        try:
            model = Order.objects.get(pk=pk)
            return Response(OrderSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)



class OrderSoftDelete(APIView):
    permission_classes = [IsAuthenticated & OrderSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Order.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class OrderForceDelete(APIView):
    permission_classes = [IsAuthenticated & OrderForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Order.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class OrderRestore(APIView):
    permission_classes = [IsAuthenticated & OrderRestorePermission]

    def put(self, request, pk):
        try:
            address = Order.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

