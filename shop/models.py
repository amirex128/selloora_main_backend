from django.db import models

from media.models import Media
from user.models import User


class Theme(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, choices=[('instagram', 'instagram'), ('website', 'website')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    media = models.ForeignKey(Media, blank=True, null=True, on_delete=models.SET_NULL, related_name='themes')

    class Meta:
        db_table = "themes"

class Shop(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.CharField(max_length=255, blank=True, null=True)
    instagram_id = models.CharField(max_length=255, blank=True, null=True)
    whatsapp_id = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    send_price = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops')
    media = models.ForeignKey(Media, blank=True, null=True, on_delete=models.SET_NULL, related_name='shops')
    theme = models.ForeignKey(Theme, default=1, on_delete=models.SET_NULL,null=True, related_name='shops')

    class Meta:
        db_table = "shops"