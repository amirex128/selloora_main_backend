from rest_framework import serializers

from shop.models import Shop
from user.models import User
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    total_sales = serializers.IntegerField(default=0)
    quantity = serializers.IntegerField(default=0)
    price = serializers.IntegerField(default=0)
    active = serializers.BooleanField(default=True)

    shop_id = serializers.IntegerField()
    media_ids = serializers.ListField(child=serializers.IntegerField())
    product_category_ids = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        shop_id = validated_data.pop('shop_id')
        media_ids = validated_data.pop('media_ids')
        product_category_ids = validated_data.pop('product_category_ids')
        product = Product.objects.create(user_id=user_id, shop_id=shop_id, **validated_data)
        product.medias.set(media_ids)
        if product_category_ids is not None:
            product.product_categories.set(product_category_ids)
        return product


class ProductUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    total_sales = serializers.IntegerField(default=0)
    quantity = serializers.IntegerField(default=0)
    price = serializers.IntegerField(default=0)
    active = serializers.BooleanField(default=True)

    media_ids = serializers.ListField(child=serializers.IntegerField())
    product_category_ids = serializers.ListField(child=serializers.IntegerField())

    def update(self, instance, validated_data):
        media_ids = validated_data.pop('media_ids')
        product_category_ids = validated_data.pop('product_category_ids')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.total_sales = validated_data.get('total_sales', instance.total_sales)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        if media_ids is not None:
            instance.medias.remove()
            instance.medias.set(media_ids)
        if product_category_ids is not None:
            instance.product_categories.set(product_category_ids)
        return instance