from django.contrib import admin
from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
