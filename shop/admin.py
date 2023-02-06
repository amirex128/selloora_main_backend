from django.contrib import admin
from .models import Shop, Theme


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
