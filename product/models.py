from django.db import models

from media.models import Media
from product_category.models import ProductCategory
from shop.models import Shop
from user.models import User


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    total_sales = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    block_status = models.CharField(default='ok', max_length=5, choices=[('block', 'block'), ('ok', 'ok')])
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    medias = models.ManyToManyField(Media, related_name='products')
    product_categories = models.ManyToManyField(ProductCategory, related_name='products')

    class Meta:
        db_table = "products"


class Option(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='options')

    class Meta:
        db_table = "options"
