from django.urls import path
from katu.views import home

urlpatterns = [
    path('', home ),
    #path('sobre/', sobre),
    #path('contatos/', contatos),
]