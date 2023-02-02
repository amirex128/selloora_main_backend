from datetime import datetime

from article.models import Article
from rest_framework import serializers

from article_category.serializers import ArticleCategorySerializer
from media.models import Media
from media.serializers import MediaSerializer
from shop.models import Shop
from shop.serializers import ShopSerializer
from user.models import User
from user.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)
    body = serializers.CharField(required=False)
    media_id = serializers.IntegerField(required=True)
    shop_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        media_id = validated_data.pop('media_id')
        shop_id = validated_data.pop('shop_id')
        validated_data['created_at'] = datetime.now()
        validated_data['updated_at'] = datetime.now()
        return Article.objects.create(user=User(id=user_id), media=Media(id=media_id), shop=Shop(id=shop_id),
                                      **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.media_id = validated_data.get('media_id', instance.media_id)
        instance.shop_id = validated_data.get('shop_id', instance.shop_id)
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = '__all__'
