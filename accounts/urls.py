from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('otp/', views.otpVerify, name='otp'),
    path('login/' , views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]