from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('', views.home, name="home"),
    path('login/',  LoginView.as_view() , {'template_name': 'login.html'}),
    path('details/<str:pk>/', views.details, name="details"),
    path('room/', views.room_aval, name="room"),
    path('confirm/', views.confirm, name="confirm")
]
