from rest_framework import serializers

from .models import City

class CityIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
            model = City
            fields = '__all__'