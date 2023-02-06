from django.urls import path

from .views import ProductCommentIndex, ProductCommentCreate, ProductCommentShow, ProductCommentForceDelete
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ProductCommentIndex.as_view()),
    path('create', ProductCommentCreate.as_view()),
    path('show/<int:pk>', ProductCommentShow.as_view()),
    path('delete/force/<int:pk>', ProductCommentForceDelete.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)