import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from user.models import User


def article_directory_path(instance, filename):
    return 'landing/articles/{}/{}'.format(instance.user.id, uuid.uuid4().hex + filename)


def category_directory_path(instance, filename):
    return 'landing/category/{}/{}'.format(instance.user.id, uuid.uuid4().hex + filename)


class LandingSetting(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')

    pricing = models.JSONField()
    faq = models.JSONField()

    class Meta:
        db_table = 'landing_config'
        ordering = ('id',)


class LandingArticle(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=250, unique=True)
    media = models.ImageField(upload_to=article_directory_path)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'landing_articles'
        ordering = ('-id',)


class LandingCategory(models.Model):
    title = models.CharField(max_length=100)
    media = models.ImageField(upload_to=category_directory_path)
    slug = models.SlugField(max_length=250, unique=True)

    articles = models.ManyToManyField('LandingArticle', related_name='categories')

    class Meta:
        db_table = 'landing_categories'
        ordering = ('-id',)


class LandingContact(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'landing_contacts'
        ordering = ('-id',)
