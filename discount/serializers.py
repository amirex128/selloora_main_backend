from rest_framework import serializers

from user.models import User
from .models import Discount

class DiscountIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class DiscountCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)
    started_at = serializers.DateTimeField()
    ended_at = serializers.DateTimeField()
    count = serializers.IntegerField()
    value = serializers.IntegerField()
    percent = serializers.IntegerField()
    status = serializers.BooleanField(default=True)
    type = serializers.ChoiceField(choices=[('percent', 'percent'), ('amount', 'amount')])
    model = serializers.ChoiceField(choices=[('shop', 'shop'), ('product', 'product')])

    product_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    shop_ids = serializers.ListField(child=serializers.IntegerField(), required=False)

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        product_ids = validated_data.pop('product_ids')
        shop_ids = validated_data.pop('shop_ids')
        discount = Discount.objects.create(user_id=user_id, **validated_data)
        if product_ids is not None:
            discount.products.set(product_ids)
        if shop_ids is not None:
            discount.shops.set(shop_ids)
        return discount


class DiscountUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)
    started_at = serializers.DateTimeField()
    ended_at = serializers.DateTimeField()
    count = serializers.IntegerField()
    value = serializers.IntegerField()
    percent = serializers.IntegerField()
    status = serializers.BooleanField(default=True)
    type = serializers.ChoiceField(choices=[('percent', 'percent'), ('amount', 'amount')])
    model = serializers.ChoiceField(choices=[('shop', 'shop'), ('product', 'product')])

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.started_at = validated_data.get('started_at', instance.started_at)
        instance.ended_at = validated_data.get('ended_at', instance.ended_at)
        instance.count = validated_data.get('count', instance.count)
        instance.value = validated_data.get('value', instance.value)
        instance.percent = validated_data.get('percent', instance.percent)
        instance.status = validated_data.get('status', instance.status)
        instance.type = validated_data.get('type', instance.type)
        instance.model = validated_data.get('model', instance.model)
        instance.save()
        product_ids = validated_data.pop('product_ids')
        shop_ids = validated_data.pop('shop_ids')
        if product_ids is not None:
            instance.products.remove()
            instance.products.set(product_ids)
        if shop_ids is not None:
            instance.shops.remove()
            instance.shops.set(shop_ids)
        return instance
