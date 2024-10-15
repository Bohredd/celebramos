from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from .forms import UsuarioCreationForm, EsqueciSenhaForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Usuario
from utils.enviar_email import enviar_email


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

def esqueci_senha(request):
    if request.method == 'POST':
        form = EsqueciSenhaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                usuario = Usuario.objects.get(email=email)
                nova_senha = get_random_string(8)
                usuario.set_password(nova_senha)
                usuario.save()

                print("Nova senha: ", nova_senha)

                # enviar_email(
                #     'Recuperação de Senha',
                #     f'Sua nova senha temporária é: {nova_senha}. Você poderá alterá-la após o login.',
                #     email
                # )

                messages.success(request, 'A nova senha foi enviada para o seu e-mail.')
                return redirect('login_usuario')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuário com esse e-mail não foi encontrado.')
    else:
        form = EsqueciSenhaForm()

    return render(request, 'usuarios/esqueci_senha.html', {'form': form})