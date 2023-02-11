from django.urls import path

from landing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('details/<slug:slug>', views.details, name='details'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
]

handler404 = "landing.views.page_not_found_view"