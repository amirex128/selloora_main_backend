from datetime import datetime

from article.models import Article
from rest_framework import serializers
from media.models import Media
from shop.models import Shop
from user.models import User


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
        validated_data['created_at'] = datetime.now()
        validated_data['updated_at'] = datetime.now()

        article_category_ids= validated_data.pop('article_category_ids')
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
        instance.updated_at = datetime.now()
        instance.media = Media(id=validated_data.get('media_id', instance.media.id))
        instance.article_category.set(validated_data.get('article_category_ids', instance.article_category.all()))
        instance.save()
        return instance