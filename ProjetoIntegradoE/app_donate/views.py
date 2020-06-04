from django.shortcuts import render, redirect
from django.apps import apps
Ong = apps.get_model('app_ong', 'Ong')


def donate(request):
    data = {}
    data['ongs'] = Ong.objects.all()
    return render(request, 'donate.html', data)


def donateType(request, pk):
    data = {}
    data['ong'] = Ong.objects.get(pk=pk)
    return render(request, 'donate_type.html', data)
