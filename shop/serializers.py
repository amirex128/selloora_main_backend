from rest_framework import serializers

from media.models import Media
from user.models import User
from .models import Shop, Theme
class ShopIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField
    phone = serializers.CharField(max_length=255,)
    mobile = serializers.CharField(max_length=255,)
    telegram_id = serializers.CharField(max_length=255,)
    instagram_id = serializers.CharField(max_length=255,)
    whatsapp_id = serializers.CharField(max_length=255,)
    email = serializers.CharField(max_length=255,)
    website = serializers.CharField(max_length=255,)
    send_price = serializers.IntegerField(default=0)
    tax = serializers.IntegerField(default=0)

    media_id = serializers.IntegerField()
    theme_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        media_id = validated_data.pop('media_id')
        theme_id = validated_data.pop('theme_id')
        return Shop.objects.create(user_id=user_id, media_id=media_id, theme=Theme(id=theme_id),
                                   **validated_data)


class ShopUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField
    phone = serializers.CharField(max_length=255,)
    mobile = serializers.CharField(max_length=255,)
    telegram_id = serializers.CharField(max_length=255,)
    instagram_id = serializers.CharField(max_length=255,)
    whatsapp_id = serializers.CharField(max_length=255,)
    email = serializers.CharField(max_length=255,)
    website = serializers.CharField(max_length=255,)
    send_price = serializers.IntegerField(default=0)
    tax = serializers.IntegerField(default=0)

    media_id = serializers.IntegerField()
    theme_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
        instance.instagram_id = validated_data.get('instagram_id', instance.instagram_id)
        instance.whatsapp_id = validated_data.get('whatsapp_id', instance.whatsapp_id)
        instance.email = validated_data.get('email', instance.email)
        instance.website = validated_data.get('website', instance.website)
        instance.send_price = validated_data.get('send_price', instance.send_price)
        instance.tax = validated_data.get('tax', instance.tax)
        instance.media = Media(id=validated_data.get('media_id', instance.media.id))
        instance.theme = Theme(id=validated_data.get('theme_id', instance.theme.id))
        instance.save()
        return instance