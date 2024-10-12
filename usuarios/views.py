from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UsuarioCreationForm, UsuarioForm, ConfiguracoesUsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from .models import ConfiguracoesUsuario


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Bem-vindo(a), {user.get_primeiro_nome()}!")
                return redirect('usuarios:perfil')
            else:
                messages.error(request, "Usuário ou senha incorretos.")
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = AuthenticationForm()

    return render(request, "usuarios/login.html", {"form": form})


@login_required
def minha_conta(request):
    usuario = request.user

    try:
        configuracoes = usuario.configuracoes
    except ConfiguracoesUsuario.DoesNotExist:
        configuracoes = ConfiguracoesUsuario.objects.create(usuario=usuario)

    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        configuracoes_form = ConfiguracoesUsuarioForm(request.POST, instance=configuracoes)

        if usuario_form.is_valid() and configuracoes_form.is_valid():
            usuario_form.save()
            configuracoes_form.save()
            return redirect('minha_conta')

    else:
        usuario_form = UsuarioForm(instance=usuario)
        configuracoes_form = ConfiguracoesUsuarioForm(instance=configuracoes)

    return render(
        request,
        "usuarios/minha_conta.html",
        {
            "usuario_form": usuario_form,
            "configuracoes_form": configuracoes_form,
        }
    )

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('usuarios:login')
    else:
        form = UsuarioCreationForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('usuarios:login')