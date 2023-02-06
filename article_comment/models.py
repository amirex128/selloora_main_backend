from django.db import models

from article.models import Article
from shop.models import Shop
from user.models import User


class ArticleComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    accept = models.CharField(max_length=8,
                              choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')],
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,related_name='article_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='article_comments')

    class Meta:
        db_table = "article_comments"
        ordering = ['-created_at']
