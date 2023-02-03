from rest_framework import serializers

from user.models import User
from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class MediaCreateSerializer(serializers.Serializer):
    file = serializers.FileField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        return Media.objects.create(user_id=user_id, **validated_data)
