from django.urls import path

from .views import ProductCategoryIndex, ProductCategoryCreate, ProductCategoryShow, ProductCategoryUpdate, ProductCategorySoftDelete, \
    ProductCategoryForceDelete, ProductCategoryRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ProductCategoryIndex.as_view()),
    path('create', ProductCategoryCreate.as_view()),
    path('show/<int:pk>', ProductCategoryShow.as_view()),
    path('update/<int:pk>', ProductCategoryUpdate.as_view()),
    path('delete/<int:pk>', ProductCategorySoftDelete.as_view()),
    path('delete/force/<int:pk>', ProductCategoryForceDelete.as_view()),
    path('delete/restore/<int:pk>', ProductCategoryRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)