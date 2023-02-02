import datetime

from django.db import models

from city.models import City
from province.models import Province


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=5, choices=(('man', 'man'), ('woman', 'woman')), blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, unique=True)
    expire_at = models.DateField(default=datetime.date(2025, 1, 1))
    status = models.CharField(max_length=5, choices=(('ok', 'ok'), ('block', 'block')), default='ok')
    verify_code = models.CharField(max_length=255, blank=True, null=True)
    cart_number = models.CharField(max_length=255, blank=True, null=True)
    shaba = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    last_send_sms_at = models.DateTimeField(blank=True, null=True)
    profile_photo_path = models.CharField(max_length=2048, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    province = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True, related_name='users')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, related_name='users')

    class Meta:
        db_table = "users"
