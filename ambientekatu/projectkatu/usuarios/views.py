from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.http import Http404
from django.http import HttpRequest

# Create your views here.

def register_view(request):
    register_form = request.session.get("register_form", None)

    form= RegisterForm()
    return render(request, 'pages/register_view.html', {'form' : form})

def register_create(request):
    if not request.POST:
        raise Http404()
    
    post = request.POST
    request.session["register_form"] = post

    form = RegisterForm(post)
    
    # form= RegisterForm()
    return render(request, 'pages/register_view.html', {'form' : form})