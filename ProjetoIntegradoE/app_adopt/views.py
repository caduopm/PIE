from django.shortcuts import render, redirect
from django.apps import apps
Animal = apps.get_model('app_animal', 'Animal')


def adopt(request):
    data = {}
    data['animals'] = Animal.objects.all()
    return render(request, 'adopt.html', data)
