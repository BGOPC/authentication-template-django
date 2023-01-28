from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views import View
from . import forms
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as authLoginView
from django.contrib.auth.views import LogoutView as authLogoutView
from tisno import settings


# Create your views here.

class UserView(LoginRequiredMixin, TemplateView):
    template_name = "users/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context edits later
        return context


class LoginView(authLoginView):
    template_name = 'users/login.html'
    authentication_form = forms.LoginForm
    redirect_authenticated_user = True

    def get_default_redirect_url(self):
        return resolve_url(settings.LOGIN_REDIRECT_URL)


class newUserView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    form_class = forms.NewUserForm
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"


class LogoutView(authLogoutView):
    template_name = "users/logout.html"

    def get_default_redirect_url(self):
        return resolve_url(settings.LOGOUT_REDIRECT_URL)
