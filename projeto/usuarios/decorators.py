from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

def login_e_ativo_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.user.is_active:
            messages.error(request, "Confirme seu email para ativar sua conta.")
            return redirect('login_usuario')
        return view_func(request, *args, **kwargs)
    return wrapper
