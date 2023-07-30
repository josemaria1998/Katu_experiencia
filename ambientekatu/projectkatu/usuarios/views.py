from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.http import Http404
from django.http import HttpRequest

# Create your views here.

def register_view(request, firstacess=0):

    if firstacess == 1:
        register_form = request.session.get("register_form", None)
        form = RegisterForm(register_form)
    else:
        if request.session.get("register_form"):
            del(request.session["register_form"])
        form = RegisterForm()

    register_form = request.session.get("register_form", None)

    form= RegisterForm()
    return render(request, 'pages/register_view.html', {'form' : form})

def register_create(request):
    if not request.POST:
        raise Http404()
    
    post = request.POST
    request.session["register_form"] = post

    form = RegisterForm(post)
    
    return redirect('usuarios:register', firstacess=1)