from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    context={}
    return render(request,'registration/login.html', context)    

  

def recuperarContrasena(request):
    context={}
    return render(request,'html/recuperarContrasena.html', context) 

def recuperarCuenta(request):
    context={}
    return render(request,'html/recuperarCuenta.html', context)
    
@login_required
def exit(request):
    logout(request)
    return redirect('')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)
