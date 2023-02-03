from django.urls import path

from .views import ArticleCommentIndex, ArticleCommentCreate, ArticleCommentShow,ArticleCommentForceDelete
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ArticleCommentIndex.as_view()),
    path('create', ArticleCommentCreate.as_view()),
    path('show/<int:pk>', ArticleCommentShow.as_view()),
    path('delete/force/<int:pk>', ArticleCommentForceDelete.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)