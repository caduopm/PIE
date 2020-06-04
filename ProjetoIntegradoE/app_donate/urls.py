from django.urls import path

from .views import donate, donateType

urlpatterns = [
    path('', donate, name='donate'),
    path('donate_type/<int:pk>', donateType, name='donateType'),
]
