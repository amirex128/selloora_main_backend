from django.db import models

from province.models import Province


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    persian_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        verbose_name_plural = 'Cities'
        db_table = "cities"