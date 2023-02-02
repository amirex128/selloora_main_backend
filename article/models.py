from django.db import models
from django.db.models.fields import related

from article_category.models import ArticleCategory
from media.models import Media
from shop.models import Shop
from user.models import User


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    media = models.ForeignKey(Media, null=True, on_delete=models.SET_NULL, related_name='articles')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='articles')
    article_category = models.ManyToManyField(ArticleCategory, related_name='articles')

    class Meta:
        db_table = "articles"