from rest_framework import serializers

from .models import Order

class OrderIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
            model = Order
            fields = '__all__'
class OrderCreateSerializer(serializers.Serializer):
    pass
