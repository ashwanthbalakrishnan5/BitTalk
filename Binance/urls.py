from django.urls import path
from . import views

urlpatterns = [
    path('positions/', views.positions, name='positions'),
    path('balance/', views.balance, name='balance'),
    path('', views.index, name='index')
]
