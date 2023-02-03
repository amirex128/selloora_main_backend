from django.contrib import admin

from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
