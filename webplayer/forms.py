from django import forms
from django.forms import PasswordInput, TextInput
from django.utils.translation import gettext_lazy as _


class PlayerForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100, widget=TextInput, required=True)
    organization = forms.CharField(label=_('Organization'), max_length=100, widget=TextInput, required=True)
    password = forms.CharField(label=_('Password'), max_length=100, widget=PasswordInput, required=False)
