from django.urls import path

from .views import ProductIndex, ProductCreate, ProductShow, ProductUpdate, ProductSoftDelete, \
    ProductForceDelete, ProductRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ProductIndex.as_view()),
    path('create', ProductCreate.as_view()),
    path('show/<int:pk>', ProductShow.as_view()),
    path('update/<int:pk>', ProductUpdate.as_view()),
    path('delete/<int:pk>', ProductSoftDelete.as_view()),
    path('delete/force/<int:pk>', ProductForceDelete.as_view()),
    path('delete/restore/<int:pk>', ProductRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)