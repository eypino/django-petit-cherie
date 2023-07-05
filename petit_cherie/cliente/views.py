from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def login(request):
    context={}
    return render(request,'html/login.html', context)    

def registro(request):
    context={}
    return render(request,'html/paginaRegistro.html', context)    

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


