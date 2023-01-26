from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView


# Create your views here.


class UserView(TemplateView):
    template_name = "users/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context edits later
        return context


def LoginView(FormView):
    pass


def newUserView(CreateView):
    pass
