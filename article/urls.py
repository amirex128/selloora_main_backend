from django.urls import path

from article.views import ArticleIndex, ArticleCreate, ArticleShow, ArticleUpdate, ArticleDelete

urlpatterns = [
    path('', ArticleIndex.as_view()),
    path('create', ArticleCreate.as_view()),
    path('show/<int:pk>', ArticleShow.as_view()),
    path('update/<int:pk>', ArticleUpdate.as_view()),
    path('delete/<int:pk>', ArticleDelete.as_view()),
]
