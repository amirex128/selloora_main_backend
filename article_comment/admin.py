from django.contrib import admin
from .models import ArticleComment


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
