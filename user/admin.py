from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
