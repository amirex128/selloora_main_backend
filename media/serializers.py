from rest_framework import serializers

from user.models import User
from .models import Media

class MediaIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class MediaCreateSerializer(serializers.Serializer):
    file = serializers.FileField()