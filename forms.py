
from django import forms


class Registro(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=20, label='Username')
    email = forms.EmailField(required=True, label='Email')
    password1 = forms.CharField(required=True, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput, label='Confirm Password')
    