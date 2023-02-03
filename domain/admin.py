from django.contrib import admin
from .models import Domain


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
