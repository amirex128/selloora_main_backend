from django.contrib import admin

from landing.models import LandingArticle, LandingSetting, LandingCategory, LandingContact


@admin.register(LandingSetting)
class LandingSettingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)


@admin.register(LandingArticle)
class LandingArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'title')
    list_filter = ('id', 'title')


@admin.register(LandingCategory)
class LandingCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'title')
    list_filter = ('id', 'title')


@admin.register(LandingContact)
class LandingContactAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id',)
    list_filter = ('id',)
