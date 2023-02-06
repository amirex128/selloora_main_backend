from rest_framework import serializers

from media.models import Media
from shop.models import Shop
from user.models import User
from .models import Ticket

class TicketIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
            model = Ticket
            fields = '__all__'
class TicketCreateSerializer(serializers.Serializer):
    is_answer = serializers.BooleanField(default=False)
    visited = serializers.BooleanField(default=False)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()

    parent_id = serializers.IntegerField()
    media_id = serializers.IntegerField()

def create(self, validated_data):
    user_id = self.context['request'].user.id
    media_id = validated_data.pop('media_id')
    return Ticket.objects.create(user_id=user_id, media_id=media_id, **validated_data)