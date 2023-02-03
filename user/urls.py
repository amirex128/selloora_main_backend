from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from user.views import UserRegisterLoginAPIView, UserVerifyCodeAPIView, UserPasswordAPIView

urlpatterns = [
    path('register-login', UserRegisterLoginAPIView.as_view()),
    path('verify-code', UserVerifyCodeAPIView.as_view()),
    path('password', UserPasswordAPIView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
