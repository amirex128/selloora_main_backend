from django.db import models

from product.models import Product
from shop.models import Shop
from user.models import User


class ProductComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    accept = models.CharField(max_length=8,
                              choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')],
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='product_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comments')

    class Meta:
        db_table = "product_comments"
