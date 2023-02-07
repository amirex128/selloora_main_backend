from django.urls import path

from .views import ArticleCategoryIndex, ArticleCategoryCreate, ArticleCategoryShow, ArticleCategoryUpdate, \
    ArticleCategorySoftDelete, \
    ArticleCategoryForceDelete, ArticleCategoryRestore, ArticleCategoryUpdateSort
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ArticleCategoryIndex.as_view()),
    path('create', ArticleCategoryCreate.as_view()),
    path('show/<int:pk>', ArticleCategoryShow.as_view()),
    path('update/<int:pk>', ArticleCategoryUpdate.as_view()),
    path('update/sort', ArticleCategoryUpdateSort.as_view()),
    path('delete/<int:pk>', ArticleCategorySoftDelete.as_view()),
    path('delete/force/<int:pk>', ArticleCategoryForceDelete.as_view()),
    path('delete/restore/<int:pk>', ArticleCategoryRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)