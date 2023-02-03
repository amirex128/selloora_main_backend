from django.urls import path

from .views import MediaIndex, MediaCreate, MediaShow, MediaSoftDelete, \
    MediaForceDelete, MediaRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', MediaIndex.as_view()),
    path('create', MediaCreate.as_view()),
    path('show/<int:pk>', MediaShow.as_view()),
    path('delete/<int:pk>', MediaSoftDelete.as_view()),
    path('delete/force/<int:pk>', MediaForceDelete.as_view()),
    path('delete/restore/<int:pk>', MediaRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)