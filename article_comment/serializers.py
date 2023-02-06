from datetime import datetime

from rest_framework import serializers

from article.models import Article
from shop.models import Shop
from user.models import User
from .models import ArticleComment

class ArticleCommentIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'


class ArticleCommentCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()

    article_id = serializers.IntegerField()
    shop_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        article_id = validated_data.pop('article_id')
        shop_id = validated_data.pop('shop_id')
        validated_data['created_at'] = datetime.now()
        return ArticleComment.objects.create(user_id=user_id, article=Article(id=article_id),
                                             shop_id=shop_id, **validated_data)
