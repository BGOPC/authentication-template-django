from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class LoginForm(AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'email'
        self.fields['username'].widget = forms.TextInput(attrs={
            "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 "
                     "mb-3 leading-tight focus:outline-none focus:bg-white",
            "placeholder": "email"
        })
        self.fields['password'].label = 'PassWord'
        self.fields['password'].widget = forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                                    "class": "appearance-none block w-full "
                                                                             "bg-gray-200 text-gray-700 border "
                                                                             "border-red-500 rounded py-3 px-4 mb-3 "
                                                                             "leading-tight focus:outline-none "
                                                                             "focus:bg-white",
                                                                    "placeholder": "Password"
                                                                    })


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 "
                 "mb-3 leading-tight focus:outline-none focus:bg-white",
        "placeholder": "email"
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].widget = forms.TextInput(attrs={
            "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 "
                     "mb-3 leading-tight focus:outline-none focus:bg-white",
            "placeholder": "FirstName"
        })
        self.fields['last_name'].label = 'Last Name'
        self.fields['last_name'].widget = forms.TextInput(attrs={
            "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 "
                     "mb-3 leading-tight focus:outline-none focus:bg-white",
            "placeholder": "LastName"
        })
        self.fields['password1'].label = 'PassWord'
        self.fields['password1'].widget = forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                                     "class": "appearance-none block w-full "
                                                                              "bg-gray-200 text-gray-700 border "
                                                                              "border-red-500 rounded py-3 px-4 mb-3 "
                                                                              "leading-tight focus:outline-none "
                                                                              "focus:bg-white",
                                                                     "placeholder": "Password"
                                                                     })
        self.fields['password2'].label = 'RePeat PassWord'
        self.fields['password2'].widget = forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                                     "class": "appearance-none block w-full "
                                                                              "bg-gray-200 text-gray-700 border "
                                                                              "border-red-500 rounded py-3 px-4 mb-3 "
                                                                              "leading-tight focus:outline-none "
                                                                              "focus:bg-white",
                                                                     "placeholder": "Repeat Password"
                                                                     })

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
        help_texts = {
            'password1': """You password shouldn't be full numeric and should have at least 8 characters"""
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
