from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.UserView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view()),
    path('login', views.LoginView.as_view(), name='login'),
    path('register/', views.newUserView.as_view()),
    path('register', views.newUserView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout', views.LogoutView.as_view()),
    path('password_reset/', views.PasswordResetView.as_view(), name='passwordReset'),
    path('password_reset', views.PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
