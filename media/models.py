from django.db import models

from user.models import User


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=255)
    full_path = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='media')


    class Meta:
        db_table = "media"