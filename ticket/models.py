from django.db import models

from media.models import Media
from user.models import User


class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.IntegerField(null=True)
    is_answer = models.BooleanField(default=False)
    visited = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tickets')
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name='tickets')

    class Meta:
        db_table = "tickets"