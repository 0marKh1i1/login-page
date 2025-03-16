from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('user/', views.UserView.as_view(), name='user'),
    path('register/', views.UserRegister.as_view(), name='register'),
    ]