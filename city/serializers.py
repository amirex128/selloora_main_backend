from province.models import Province
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'