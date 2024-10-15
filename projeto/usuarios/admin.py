from django.contrib import admin
from .models import Usuario, ConfiguracoesUsuario, Transacao

admin.site.register(Usuario)
admin.site.register(ConfiguracoesUsuario)
admin.site.register(Transacao)