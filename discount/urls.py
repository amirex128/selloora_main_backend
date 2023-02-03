from django.urls import path

from .views import DiscountIndex, DiscountCreate, DiscountShow, DiscountUpdate, DiscountSoftDelete, \
    DiscountForceDelete, DiscountRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', DiscountIndex.as_view()),
    path('create', DiscountCreate.as_view()),
    path('show/<int:pk>', DiscountShow.as_view()),
    path('update/<int:pk>', DiscountUpdate.as_view()),
    path('delete/<int:pk>', DiscountSoftDelete.as_view()),
    path('delete/force/<int:pk>', DiscountForceDelete.as_view()),
    path('delete/restore/<int:pk>', DiscountRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)