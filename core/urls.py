"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('admin/', admin.site.urls),

    path('api/v1/address/', include('address.urls')),
    path('api/v1/article/', include('article.urls')),
    path('api/v1/article_category/', include('article_category.urls')),
    path('api/v1/article_comment/', include('article_comment.urls')),
    path('api/v1/city/', include('city.urls')),
    path('api/v1/customer/', include('customer.urls')),
    path('api/v1/discount/', include('discount.urls')),
    path('api/v1/domain/', include('domain.urls')),
    path('api/v1/media/', include('media.urls')),
    path('api/v1/order/', include('order.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/product_category/', include('product_category.urls')),
    path('api/v1/product_comment/', include('product_comment.urls')),
    path('api/v1/province/', include('province.urls')),
    path('api/v1/shop/', include('shop.urls')),
    path('api/v1/ticket/', include('ticket.urls')),
    path('api/v1/user/', include('user.urls')),
]
