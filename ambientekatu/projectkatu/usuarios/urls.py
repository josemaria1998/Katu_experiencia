from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('register/', register_view, name = 'register'),
]