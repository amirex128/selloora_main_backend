from django.db import models

from city.models import City
from province.models import Province
from user.models import User


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, related_name='addresses')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='addresses')

    class Meta:
        db_table = "addresses"
        ordering = ['-created_at']
