from datetime import datetime

from rest_framework import serializers

from address.models import Address
from city.serializers import CitySerializer
from province.serializers import ProvinceSerializer
from user.models import User
from user.serializers import UserSerializer


class AddressSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)
    address = serializers.CharField(max_length=255, required=True)
    postal_code = serializers.CharField(max_length=255, required=True)
    mobile = serializers.CharField(max_length=255, required=True)
    full_name = serializers.CharField(max_length=255, required=True)
    lat = serializers.CharField(max_length=255, required=False)
    long = serializers.CharField(max_length=255, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    province_id = serializers.IntegerField(required=True)
    city_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        validated_data['created_at'] = datetime.now()
        address = Address.objects.create(user=User(id=user_id), **validated_data)
        return address

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
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance

    class Meta:
        model = Address
        fields = '__all__'
