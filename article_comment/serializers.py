from rest_framework import serializers

from article_comment.models import ArticleComment


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'