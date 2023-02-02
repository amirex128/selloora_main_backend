from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view(['GET', 'POST'])
def user_categories(request):
    if request.method == 'GET':
        categories = Category.objects.filter(
            user_id=request.user.id,
            shop_id=request.GET.get('shop_id')
        ).order_by('-created_at').paginate(
            request.GET.get('per_page', 10)
        )
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'shop_id': request.data.get('shop_id'),
            'user_id': request.user.id
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'sort': request.data.get('sort')
        }
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)