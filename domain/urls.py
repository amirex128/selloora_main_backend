from django.urls import path

from .views import DomainIndex, DomainCreate, DomainShow, DomainSoftDelete, \
    DomainForceDelete, DomainRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', DomainIndex.as_view()),
    path('create', DomainCreate.as_view()),
    path('show/<int:pk>', DomainShow.as_view()),
    path('delete/<int:pk>', DomainSoftDelete.as_view()),
    path('delete/force/<int:pk>', DomainForceDelete.as_view()),
    path('delete/restore/<int:pk>', DomainRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)