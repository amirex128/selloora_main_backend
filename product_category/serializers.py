from rest_framework import serializers

from shop.models import Shop
from user.models import User
from .models import ProductCategory

class ProductCategoryIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = ProductCategory
            fields = '__all__'
class ProductCategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()

    shop_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        shop_id = validated_data.pop('shop_id')
        return ProductCategory.objects.create(user_id=user_id, shop_id=shop_id, **validated_data)
class ProductCategoryUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    sort = serializers.IntegerField()
    description = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sort = validated_data.get('sort', instance.sort)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance