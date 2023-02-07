from django.utils import timezone
from rest_framework import serializers

from shop.models import Shop
from user.models import User
from .models import ArticleCategory


class ArticleCategoryIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


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
        last_sort = ArticleCategory.objects.filter(shop_id=shop_id).order_by('-sort').values('sort').first()
        if last_sort is not None:
            last_sort = last_sort['sort'] + 1
        else:
            last_sort = 1
        validated_data['created_at'] = timezone.now()
        validated_data['updated_at'] = timezone.now()
        return ArticleCategory.objects.create(user_id=user_id, shop_id=shop_id, sort=last_sort,
                                              **validated_data)


class ArticleCategoryUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = timezone.now()
        instance.save()
        return instance


class ArticleCategoryUpdateSortSerializer(serializers.Serializer):
    sorts = serializers.JSONField()