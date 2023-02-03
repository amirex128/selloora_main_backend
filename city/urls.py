from django.urls import path

from .views import CityIndex
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', CityIndex.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)