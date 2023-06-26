from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Email'),
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 '
                     'mb-3 leading-tight focus:outline-none focus:bg-white text-center',
            'placeholder': _('Email')
        })
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 '
                     'mb-3 leading-tight focus:outline-none focus:bg-white text-center',
            'placeholder': _('Password')
        })
    )


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs={
            'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 '
                     'mb-3 leading-tight focus:outline-none text-center focus:bg-white',
            'placeholder': _('Email')
        })
    )
    phone = PhoneNumberField(
        label=_('Phone number'),
        required=True,
        region='IR',
        widget=PhoneNumberPrefixWidget(
            initial='IR',
            attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-center text-gray-700 border border-red-500 '
                         'rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                'placeholder': _('Phone number')
            }
        )
    )

    first_name = forms.CharField(
        label=_('First Name'),
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 '
                     'mb-3 leading-tight focus:outline-none text-center focus:bg-white',
            'placeholder': _('First Name')
        })
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 '
                     'mb-3 leading-tight focus:outline-none text-center focus:bg-white',
            'placeholder': _('Last Name')
        })
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 '
                     'mb-3 leading-tight focus:outline-none focus:bg-white text-center',
            'placeholder': _('Password')
        }),
        help_text=_("Your password should not be fully numeric and should have at least 8 characters.")
    )
    password2 = forms.CharField(
        label=_('Repeat Password'),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 '
                     'mb-3 leading-tight focus:outline-none focus:bg-white text-center',
            'placeholder': _('Repeat Password')
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
