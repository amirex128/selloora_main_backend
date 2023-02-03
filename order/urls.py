from django.urls import path

from .views import OrderIndex, OrderCreate, OrderShow, OrderSoftDelete, \
    OrderForceDelete, OrderRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', OrderIndex.as_view()),
    path('create', OrderCreate.as_view()),
    path('show/<int:pk>', OrderShow.as_view()),
    path('delete/<int:pk>', OrderSoftDelete.as_view()),
    path('delete/force/<int:pk>', OrderForceDelete.as_view()),
    path('delete/restore/<int:pk>', OrderRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)