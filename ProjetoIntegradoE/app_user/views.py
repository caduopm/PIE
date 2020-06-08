from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import User
from .form import UserForm


# Create your views here.
def user(request):
    data = {}
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    data['form'] = form
    return render(request, 'user.html', data)