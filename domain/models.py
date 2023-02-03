from django.db import models

from shop.models import Shop
from user.models import User


class Domain(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[('subdomain', 'Subdomain'), ('domain', 'Domain')])
    dns_status = models.CharField(max_length=255,
                                  choices=[('pending', 'Pending'), ('verified', 'Verified'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='domains')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='domains')

    class Meta:
        db_table = "domains"
