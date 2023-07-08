from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login  

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio después del inicio de sesión exitoso
        else:
            # El usuario no es válido, mostrar un mensaje de error
            context = {'error_message': 'Credenciales inválidas'}
            return render(request, 'registration/login.html', context)
    else:
        context = {}
        return render(request, 'registration/login.html', context)
  

def recuperarContrasena(request):
    context = {}
    return render(request, 'html/recuperarContrasena.html', context) 

def recuperarCuenta(request):
    context = {}
    return render(request, 'html/recuperarCuenta.html', context)
    
@login_required
def exit(request):
    logout(request)
    return redirect('index')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            auth_login(request, user)  
            return redirect('index')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)