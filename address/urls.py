from django.urls import path

from .views import AddressIndex, AddressCreate, AddressShow, AddressUpdate, AddressSoftDelete, \
    AddressForceDelete, AddressRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', AddressIndex.as_view()),
    path('create', AddressCreate.as_view()),
    path('show/<int:pk>', AddressShow.as_view()),
    path('update/<int:pk>', AddressUpdate.as_view()),
    path('delete/<int:pk>', AddressSoftDelete.as_view()),
    path('delete/force/<int:pk>', AddressForceDelete.as_view()),
    path('delete/restore/<int:pk>', AddressRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)