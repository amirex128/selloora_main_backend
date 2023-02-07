
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Ticket
from .permissions import TicketIndexPermission, TicketCreatePermission, TicketShowPermission, TicketSoftDeletePermission, TicketForceDeletePermission, \
    TicketRestorePermission
from .serializers import TicketCreateSerializer, TicketSerializer, TicketIndexSerializer


class TicketIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & TicketIndexPermission]

    def get(self, request):
        try:
            model = Ticket.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(TicketIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class TicketCreate(APIView):
    permission_classes = [IsAuthenticated & TicketCreatePermission]

    def post(self, request):
        try:
            serializer = TicketCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                result = serializer.save()
                return Response({
                    'message': messages.CREATED,
                    'data': TicketSerializer(result).data
                })
            else:
                return Response(serializer.errors)
        except Exception as e:
            return exceptions.default_exception(self, e)



class TicketShow(APIView):
    permission_classes = [IsAuthenticated & TicketShowPermission]

    def get(self, request, pk):
        try:
            model = Ticket.objects.get(pk=pk)
            return Response(TicketSerializer(model).data)
        except Exception as e:
            return exceptions.default_exception(self, e)


class TicketSoftDelete(APIView):
    permission_classes = [IsAuthenticated & TicketSoftDeletePermission]

    def delete(self, request, pk):
        try:
            model = Ticket.objects.get(pk=pk)
            model.deleted_at = timezone.now()
            model.save()
            return Response({
                'message': messages.DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class TicketForceDelete(APIView):
    permission_classes = [IsAuthenticated & TicketForceDeletePermission]

    def delete(self, request, pk):
        try:
            address = Ticket.objects.get(pk=pk)
            address.delete()
            return Response({
                'message': messages.FORCE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)



class TicketRestore(APIView):
    permission_classes = [IsAuthenticated & TicketRestorePermission]

    def put(self, request, pk):
        try:
            address = Ticket.objects.get(pk=pk)
            address.deleted_at = None
            address.save()
            return Response({
                'message': messages.RESTORE_DELETED
            })
        except Exception as e:
            return exceptions.default_exception(self, e)

