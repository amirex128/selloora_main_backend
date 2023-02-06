from django.db import models

from product.models import Product
from shop.models import Shop
from user.models import User


class Discount(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=255)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    count = models.IntegerField()
    value = models.IntegerField()
    percent = models.IntegerField()
    status = models.BooleanField(default=True)
    type = models.CharField(max_length=255, choices=[('percent', 'percent'), ('amount', 'amount')])
    model = models.CharField(max_length=255, choices=[('shop', 'shop'), ('product', 'product')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discounts')
    products = models.ManyToManyField(Product, related_name='discounts')
    shops = models.ManyToManyField(Shop, related_name='discounts')

    class Meta:
        db_table = "discounts"
        ordering = ['-created_at']
