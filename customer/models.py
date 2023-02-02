from django.db import models

from city.models import City
from province.models import Province


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    verify_code = models.CharField(max_length=255, blank=True, null=True)
    last_send_sms_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    province = models.ForeignKey(Province, on_delete=models.SET_NULL,null=True,related_name='customers')
    city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True,related_name='customers')

    class Meta:
        db_table = "customers"

    def __str__(self):
        return self.full_name