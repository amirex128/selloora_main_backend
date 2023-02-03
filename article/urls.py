from django.urls import path

from .views import ArticleIndex, ArticleCreate, ArticleShow, ArticleUpdate, ArticleSoftDelete, \
    ArticleForceDelete, ArticleRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ArticleIndex.as_view()),
    path('create', ArticleCreate.as_view()),
    path('show/<int:pk>', ArticleShow.as_view()),
    path('update/<int:pk>', ArticleUpdate.as_view()),
    path('delete/<int:pk>', ArticleSoftDelete.as_view()),
    path('delete/force/<int:pk>', ArticleForceDelete.as_view()),
    path('delete/restore/<int:pk>', ArticleRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)