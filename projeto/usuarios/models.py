from __future__ import annotations
from django.contrib.auth.models import AbstractUser
from django.db import models
from usuarios.managers import UsuarioManager
from django.templatetags.static import static


class Usuario(AbstractUser):
    username = None
    first_name = None
    last_name = None
    nome_completo = models.CharField(
        "Nome Completo", max_length=100, blank=False, null=False
    )
    email = models.EmailField("E-mail", blank=True, unique=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)  # (11) 98765-4321
    data_nascimento = models.DateField("Data de  Nascimento", blank=True, null=True)
    imagem = models.ImageField(blank=True, null=True, upload_to="usuarios/images")
    creditos = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome_completo"]

    objects = UsuarioManager()

    def __str__(self):
        return self.nome_completo

    def get_primeiro_nome(self):
        return self.nome_completo.split(" ")[0]

class ConfiguracoesUsuario(models.Model):

    tema = models.CharField(
        max_length=200,
        choices=(
            ('escuro', 'Escuro'),
            ('claro', 'Claro')
        ),
        default='claro',
    )
    notificacoes_itens = models.BooleanField(default=False) # quando item for marcado como comprado (item)
    notificacoes_renovacao = models.BooleanField(default=False)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='configuracoes')

    def get_theme(self):
        if self.tema == 'claro':
            return static('css/tema-padrao.css')
        else:
            return static('css/tema-escuro.css')

class Transacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    creditos_movimentados = models.DecimalField(max_digits=10, decimal_places=0)
    is_compra = models.BooleanField(default=False)
    is_debito = models.BooleanField(default=False)

    # if is compra
    plano_comprado = models.ForeignKey('wishlists.PlanoCredito', on_delete=models.CASCADE, null=True, blank=True)

    # if is debito
    wishlist = models.ForeignKey('wishlists.Wishlist', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.usuario} - {self.creditos_movimentados} - {self.data}'