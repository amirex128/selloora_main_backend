from django.utils import timezone

from article.models import Article
from rest_framework import serializers
from media.models import Media


class ArticleIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()

    shop_id = serializers.IntegerField()
    media_id = serializers.IntegerField()
    article_category_ids = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        shop_id = validated_data.pop('shop_id')
        media_id = validated_data.pop('media_id')
        validated_data['created_at'] = timezone.now()
        validated_data['updated_at'] = timezone.now()

        article_category_ids = validated_data.pop('article_category_ids')
        article = Article.objects.create(user_id=user_id, shop_id=shop_id, media_id=media_id, **validated_data)
        article.article_category.set(article_category_ids)
        return article


class ArticleUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    media_id = serializers.IntegerField()
    article_category_ids = serializers.ListField(child=serializers.IntegerField())

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.updated_at = timezone.now()
        instance.media = Media(id=validated_data.get('media_id', instance.media.id))
        instance.article_category.set(validated_data.get('article_category_ids', instance.article_category.all()))
        instance.save()
        return instance
