from django.shortcuts import render, redirect
from django.forms import ModelForm
from .form import LoginForm
from django.apps import apps
User = apps.get_model('app_user', 'User')


def login(request):
    isValid = False
    data = {}
    data['showErrorMessege'] = True
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            obj = [
                form.cleaned_data['email'], 
                form.cleaned_data['password']
            ]

            for user in User.objects.all():
                if user.email == obj[0]:
                    if user.password == obj[1]:
                        isValid = True

            if isValid:
                return redirect('index')
            else:
                data['showErrorMessege'] = False

    data['form'] = form
    return render(request, 'login.html', data)


def register(request):
    return render(request, 'register.html')


def registerOng1(request):
    return render(request, 'register_ong_1.html')


def registerOng2(request):
    return render(request, 'register_ong_2.html')


def registerUser1(request):
    return render(request, 'register_user_1.html')


def registerUser2(request):
    return render(request, 'register_user_2.html')


def resetPassword(request):
    return render(request, 'reset_password.html')
