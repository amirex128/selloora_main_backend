from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket
from .permissions import TicketIndexPermission, TicketCreatePermission, TicketShowPermission, TicketSoftDeletePermission, TicketForceDeletePermission, \
    TicketRestorePermission
from .serializers import TicketCreateSerializer, TicketSerializer


class TicketIndex(APIView):
    permission_classes = [IsAuthenticated & TicketIndexPermission]

    def get(self, request):
        addresses = TicketSerializer(Ticket.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class TicketCreate(APIView):
    permission_classes = [IsAuthenticated & TicketCreatePermission]

    def post(self, request):
        serializer = TicketCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TicketShow(APIView):
    permission_classes = [IsAuthenticated & TicketShowPermission]

    def get(self, request, pk):
        address = Ticket.objects.get(pk=pk)
        return Response(address)

class TicketSoftDelete(APIView):
    permission_classes = [IsAuthenticated & TicketSoftDeletePermission]

    def delete(self, request, pk):
        address = Ticket.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class TicketForceDelete(APIView):
    permission_classes = [IsAuthenticated & TicketForceDeletePermission]

    def delete(self, request, pk):
        address = Ticket.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class TicketRestore(APIView):
    permission_classes = [IsAuthenticated & TicketRestorePermission]

    def put(self, request, pk):
        address = Ticket.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
