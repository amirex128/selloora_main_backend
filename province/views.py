from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Province
from .permissions import ProvinceIndexPermission
from .serializers import ProvinceSerializer


class ProvinceIndex(APIView):
    permission_classes = [IsAuthenticated & ProvinceIndexPermission]

    def get(self, request):
        addresses = ProvinceSerializer(Province.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)
