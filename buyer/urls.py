from django.urls import path
from . import views
urlpatterns = [

    path('registration/', views.registration, name='registration'),
    path('index/about', views.about, name='about'),
    path('checkout', views.checkout, name='checkout'),
    path('index/contact', views.contact, name='contact'),
    path('index/faqs/', views.faqs, name='faqs'),
    path('index/', views.index, name='index'),
    path('index/payment/', views.payment, name='payment'),
    path('index/privacy/', views.privacy, name='privacy'),
    path('index/product/', views.product, name='product'),
    path('product2/', views.product2, name='product2'),
    path('single/', views.single, name='single'),
    path('single2/', views.single2, name='single2'),
    path('index/terms/', views.terms, name='terms'),
    path('', views.login, name='login'),
    path('otp/', views.otp, name='otp'),

]
