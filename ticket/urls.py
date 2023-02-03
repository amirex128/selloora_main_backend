from django.urls import path

from .views import TicketIndex, TicketCreate, TicketShow, TicketSoftDelete, \
    TicketForceDelete, TicketRestore
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', TicketIndex.as_view()),
    path('create', TicketCreate.as_view()),
    path('show/<int:pk>', TicketShow.as_view()),
    path('delete/<int:pk>', TicketSoftDelete.as_view()),
    path('delete/force/<int:pk>', TicketForceDelete.as_view()),
    path('delete/restore/<int:pk>', TicketRestore.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)