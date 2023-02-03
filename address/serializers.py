from datetime import datetime

from rest_framework import serializers

from address.models import Address
from city.models import City
from province.models import Province
from user.models import User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
            model = Address
            fields = '__all__'

class AddressCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    address = serializers.CharField(max_length=255, required=True)
    postal_code = serializers.CharField(max_length=255, required=True)
    mobile = serializers.CharField(max_length=255, required=True)
    full_name = serializers.CharField(max_length=255, required=True)
    lat = serializers.CharField(max_length=255, required=False)
    long = serializers.CharField(max_length=255, required=False)

    province_id = serializers.IntegerField(required=True)
    city_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        province_id = validated_data.pop('province_id')
        city_id = validated_data.pop('city_id')
        validated_data['created_at'] = datetime.now()
        validated_data['updated_at'] = datetime.now()
        return Address.objects.create(user_id=user_id, province_id=province_id, city_id=city_id, **validated_data)


class AddressUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(max_length=255, required=False)
    postal_code = serializers.CharField(max_length=255, required=False)
    mobile = serializers.CharField(max_length=255, required=False)
    full_name = serializers.CharField(max_length=255, required=False)
    lat = serializers.CharField(max_length=255, required=False)
    long = serializers.CharField(max_length=255, required=False)

    province_id = serializers.IntegerField(required=False)
    city_id = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.address = validated_data.get('address', instance.address)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.long = validated_data.get('long', instance.long)
        instance.province_id = validated_data.get('province_id', instance.province_id)
        instance.city_id = validated_data.get('city_id', instance.city_id)
        instance.updated_at = datetime.now()
        instance.save()
        return instance