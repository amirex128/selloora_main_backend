from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductComment
from .permissions import ProductCommentIndexPermission, ProductCommentCreatePermission, ProductCommentShowPermission, \
    ProductCommentUpdatePermission, ProductCommentSoftDeletePermission, ProductCommentForceDeletePermission, \
    ProductCommentRestorePermission
from .serializers import ProductCommentCreateSerializer, ProductCommentSerializer


class ProductCommentIndex(APIView):
    permission_classes = [IsAuthenticated & ProductCommentIndexPermission]

    def get(self, request):
        addresses = ProductCommentSerializer(ProductComment.objects.filter(deleted_at__isnull=True), many=True)
        return Response(addresses)


class ProductCommentCreate(APIView):
    permission_classes = [IsAuthenticated & ProductCommentCreatePermission]

    def post(self, request):
        serializer = ProductCommentCreateSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductCommentShow(APIView):
    permission_classes = [IsAuthenticated & ProductCommentShowPermission]

    def get(self, request, pk):
        address = ProductComment.objects.get(pk=pk)
        return Response(address)

class ProductCommentSoftDelete(APIView):
    permission_classes = [IsAuthenticated & ProductCommentSoftDeletePermission]

    def delete(self, request, pk):
        address = ProductComment.objects.get(pk=pk)
        address.deleted_at = datetime.now()
        address.save()
        return Response('Deleted')


class ProductCommentForceDelete(APIView):
    permission_classes = [IsAuthenticated & ProductCommentForceDeletePermission]

    def delete(self, request, pk):
        address = ProductComment.objects.get(pk=pk)
        address.delete()
        return Response('Deleted')


class ProductCommentRestore(APIView):
    permission_classes = [IsAuthenticated & ProductCommentRestorePermission]

    def put(self, request, pk):
        address = ProductComment.objects.get(pk=pk)
        address.deleted_at = None
        address.save()
        return Response('Restored')
