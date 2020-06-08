from django.urls import path

from .views import user

urlpatterns = [
    path('', user, name='user'),
]