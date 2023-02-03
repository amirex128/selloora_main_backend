from rest_framework import serializers

from product.models import Product
from shop.models import Shop
from user.models import User
from .models import ProductComment


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = '__all__'


class ProductCommentCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()

    shop_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        shop_id = validated_data.pop('shop_id')
        product_id = validated_data.pop('product_id')
        return ProductComment.objects.create(user_id=user_id, shop_id=shop_id,
                                             product=Product(id=product_id), **validated_data)
