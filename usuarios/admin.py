from django.contrib import admin
from .models import Usuario, ConfiguracoesUsuario

admin.site.register(Usuario)
admin.site.register(ConfiguracoesUsuario)