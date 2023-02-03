from django.db import models

from shop.models import Shop
from user.models import User


class ArticleCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sort = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_categories')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='article_categories')

    class Meta:
        db_table = "article_categories"
