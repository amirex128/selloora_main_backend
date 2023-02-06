import datetime

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from city.models import City
from province.models import Province


class User(AbstractUser):
    gender = models.CharField(max_length=5, choices=(('man', 'man'), ('woman', 'woman')), blank=True, null=True)
    expire_at = models.DateField(default=datetime.date(2025, 1, 1))
    status = models.CharField(max_length=5, choices=(('ok', 'ok'), ('block', 'block')), default='ok')
    verify_code = models.CharField(max_length=255, blank=True, null=True)
    cart_number = models.CharField(max_length=255, blank=True, null=True)
    shaba = models.CharField(max_length=255, blank=True, null=True)
    last_send_sms_at = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    type=models.CharField(max_length=10,choices=(('user','user'),('customer','customer'),('admin','admin')),default='user')
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True, related_name='users')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, related_name='users')
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        ordering = ['-id']
