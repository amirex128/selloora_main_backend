from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City
from .permissions import CityIndexPermission
from .serializers import CitySerializer


class CityIndex(APIView):
    permission_classes = [IsAuthenticated & CityIndexPermission]

    def get(self, request):
        addresses = CitySerializer(City.objects.filter(), many=True)
        return Response(addresses)
