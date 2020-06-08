from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=16)