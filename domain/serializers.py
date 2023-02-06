from rest_framework import serializers

from shop.models import Shop
from user.models import User
from .models import Domain

class DomainIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'


class DomainCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.ChoiceField(choices=[('subdomain', 'Subdomain'), ('domain', 'Domain')])
    dns_status = serializers.ChoiceField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('failed', 'Failed')])
    shop_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        shop_id = validated_data.pop('shop_id')
        domain = Domain.objects.create(user_id=user_id, shop_id=shop_id, **validated_data)
        return domain
