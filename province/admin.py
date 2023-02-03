from django.contrib import admin
from .models import Province


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
