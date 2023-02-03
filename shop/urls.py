from django.urls import path

from .views import ShopIndex, ShopCreate, ShopShow, ShopUpdate, ShopSoftDelete, \
    ShopForceDelete, ShopRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ShopIndex.as_view()),
    path('create', ShopCreate.as_view()),
    path('show/<int:pk>', ShopShow.as_view()),
    path('update/<int:pk>', ShopUpdate.as_view()),
    path('delete/<int:pk>', ShopSoftDelete.as_view()),
    path('delete/force/<int:pk>', ShopForceDelete.as_view()),
    path('delete/restore/<int:pk>', ShopRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)