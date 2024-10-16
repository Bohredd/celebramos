from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .forms import UsuarioCreationForm, EsqueciSenhaForm, UsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario
from utils.enviar_email import enviar_email
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from decouple import config

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)

            if config("DEBUG") == 'False':
                usuario.is_active = False
                usuario.save()

                current_site = get_current_site(request)
                mail_subject = 'Ative sua conta no nosso site'
                message = render_to_string('usuarios/confirmacao_email.html', {
                    'user': usuario,
                    'domain': current_site.domain,
                    'uidb64': urlsafe_base64_encode(force_bytes(usuario.pk)),
                    'token': default_token_generator.make_token(usuario),
                })

                enviar_email(mail_subject, message, usuario.email)
            else:
                usuario.is_active = True
                usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso! Verifique seu e-mail para ativar sua conta.')
            return redirect('login_usuario')
    else:
        form = UsuarioCreationForm()

    return render(request, 'usuarios/cadastro_usuario.html', {'form': form})


UserModel = get_user_model()


def ativar_conta(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        usuario = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        usuario = None

    if usuario is not None and default_token_generator.check_token(usuario, token):
        usuario.is_active = True
        usuario.save()
        messages.success(request, 'Sua conta foi ativada com sucesso! Você já pode fazer login.')
        return redirect('login_usuario')
    else:
        messages.error(request, 'O link de ativação é inválido ou expirou.')
        return redirect('cadastro_usuario')


def login_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Autenticação realizada com sucesso.')
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
                print("Email: ", email)

                enviar_email(
                    'Recuperação de Senha',
                    f'Sua nova senha temporária é: {nova_senha}. Você poderá alterá-la após o login.',
                    email
                )

                messages.success(request, 'A nova senha foi enviada para o seu e-mail.')
                return redirect('login_usuario')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuário com esse e-mail não foi encontrado.')
    else:
        form = EsqueciSenhaForm()

    return render(request, 'usuarios/esqueci_senha.html', {'form': form})


def minha_conta(request):
    usuario = Usuario.objects.get(email=request.user.email)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações atualizadas com sucesso.')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/minha_conta.html', {'form': form, 'creditos': usuario.creditos})
