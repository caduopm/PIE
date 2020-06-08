from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'cell', 'dt_birthday', 'cpf', 'image']