from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view()),
    path('login', views.LoginView.as_view(), name='login'),
    path('register/', views.newUserView.as_view()),
    path('register', views.newUserView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout', views.LogoutView.as_view()),
]
