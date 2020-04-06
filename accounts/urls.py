from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('', views.home, name="home"),
    path('login/', views.login),
    path('details/<str:pk>/', views.details, name="details"),
    path('room/<int:ro>', views.room_aval, name="room"),
    path('confirm/<int:pk1>/<str:pk2>/', views.confirm, name="confirm")
]