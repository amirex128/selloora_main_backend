
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import messages, exceptions
from utils import debuger
from .models import Province
from .permissions import ProvinceIndexPermission
from .serializers import  ProvinceIndexSerializer


class ProvinceIndex(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated & ProvinceIndexPermission]

    def get(self, request):
        try:
            model = Province.objects.filter(user_id=request.user.id)
            self.page_size = request.GET.get('page_size', 10)
            is_deleted = bool(request.GET.get('is_deleted', False))
            if is_deleted:
                model = model.filter(deleted_at__isnull=True)
            else:
                model = model.filter(deleted_at__isnull=False)
            result = self.paginate_queryset(model, request)
            return self.get_paginated_response(ProvinceIndexSerializer(result, many=True).data)
        except Exception as e:
            return exceptions.default_exception(self, e)
