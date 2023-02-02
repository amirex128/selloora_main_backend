from django.db import models


class Province(models.Model):
    id = models.BigAutoField(primary_key=True)
    persian_name = models.CharField(max_length=150)
    english_name = models.CharField(max_length=150)
    COD = models.CharField(max_length=150)

    def __str__(self):
        return self.persian_name

    class Meta:
        db_table = "provinces"