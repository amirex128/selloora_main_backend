from rest_framework import serializers

from product_comment.models import ProductComment


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = '__all__'