from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('', views.home, name="home"),
    path('login/', views.login),
    path('details/', views.details, name="details"),
    path('room/', views.room_aval, name="room"),
    path('confirm/<str:pk>/', views.confirm, name="confirm")
]