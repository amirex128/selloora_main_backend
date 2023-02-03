from django.contrib import admin
from .models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
