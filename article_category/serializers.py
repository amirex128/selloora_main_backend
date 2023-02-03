from datetime import datetime

from rest_framework import serializers

from shop.models import Shop
from user.models import User
from .models import ArticleCategory


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleCategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)

    shop_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        shop_id = validated_data.pop('shop_id')
        validated_data['created_at'] = datetime.now()
        validated_data['updated_at'] = datetime.now()
        return ArticleCategory.objects.create(user_id=user_id, shop_id=shop_id,
                                              **validated_data)


class ArticleCategoryUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    sort = serializers.IntegerField()
    description = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sort = validated_data.get('sort', instance.sort)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = datetime.now()
        instance.save()
        return instance