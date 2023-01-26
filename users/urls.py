from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='UserHome'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.newUserView.as_view(), name='register'),
]