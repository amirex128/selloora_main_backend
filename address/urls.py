from django.urls import path

from address.views import AddressIndex, AddressCreate, AddressShow, AddressUpdate, AddressDelete

urlpatterns = [
    path('', AddressIndex.as_view()),
    path('create', AddressCreate.as_view()),
    path('show/<int:pk>', AddressShow.as_view()),
    path('update/<int:pk>', AddressUpdate.as_view()),
    path('delete/<int:pk>', AddressDelete.as_view()),
]
