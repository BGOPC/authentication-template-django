from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as authLoginView
from django.contrib.auth.views import PasswordResetView as authPasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import resolve_url, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from tisno import settings
from . import forms


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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

    def post(self, request):
        logout(request)
        return redirect('home')


class PasswordResetView(authPasswordResetView, SuccessMessageMixin):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')
