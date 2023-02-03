from django.urls import path

from .views import ProvinceIndex
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ProvinceIndex.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)