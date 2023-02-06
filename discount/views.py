
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Discount
from .permissions import DiscountIndexPermission, DiscountCreatePermission, DiscountShowPermission, \
    DiscountUpdatePermission, DiscountSoftDeletePermission, DiscountForceDeletePermission, \
    DiscountRestorePermission
from .serializers import DiscountCreateSerializer, DiscountUpdateSerializer, DiscountSerializer, DiscountIndexSerializer


class DiscountIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & DiscountIndexPermission]

    def get(self, request):
        try:
            model = Discount.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(DiscountIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class DiscountCreate(APIView):
    permission_classes = [IsAuthenticated & DiscountCreatePermission]

    def post(self, request):
        try:
            serializer = DiscountCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': DiscountIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class DiscountShow(APIView):
    permission_classes = [IsAuthenticated & DiscountShowPermission]

    def get(self, request, pk):
        try:
            model = Discount.objects.select_related('province', 'city').get(pk=pk)
            return Response(DiscountSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)



class DiscountUpdate(APIView):
    permission_classes = [IsAuthenticated & DiscountUpdatePermission]

    def put(self, request, pk):
        try:
            model = Discount.objects.get(pk=pk)
            serializer = DiscountUpdateSerializer(model, data=request.data)
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.UPDATED,
                    'data': DiscountIndexSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class DiscountSoftDelete(APIView):
    permission_classes = [IsAuthenticated & DiscountSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Discount.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class DiscountForceDelete(APIView):
    permission_classes = [IsAuthenticated & DiscountForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Discount.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class DiscountRestore(APIView):
    permission_classes = [IsAuthenticated & DiscountRestorePermission]

    def put(self, request, pk):
        try:
            address = Discount.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

