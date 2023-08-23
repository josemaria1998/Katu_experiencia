from django.urls import path
from katu.views import *

urlpatterns = [
    path('', home, name='home'),
    path('noticia/', noticia, name='noticia'),
    path('pacotes/', pacotes, name= 'pacotes'),
    path('contato/', contato, name= 'contato'),
]