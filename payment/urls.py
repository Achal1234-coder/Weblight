from django.urls import path

from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('history/', views.payement_history),
    path('data_visualization/', views.data_visualization)
]