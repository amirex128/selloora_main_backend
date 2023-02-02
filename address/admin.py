from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
