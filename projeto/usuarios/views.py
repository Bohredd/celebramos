from django.shortcuts import render, redirect
from .forms import UsuarioCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login_usuario')
    else:
        form = UsuarioCreationForm()

    return render(request, 'usuarios/cadastro_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('pagina_inicial')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'usuarios/login_usuario.html')