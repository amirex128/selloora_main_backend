
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import City
from .permissions import CityIndexPermission
from .serializers import  CityIndexSerializer


class CityIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & CityIndexPermission]

    def get(self, request):
        try:
            model = City.objects.filter(deleted_at__isnull=True,user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(CityIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)
