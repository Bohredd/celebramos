from django.db import models

class Item(models.Model):
    nome_item = models.CharField(max_length=100)
    link_compra = models.URLField(blank=True, null=True)
    comprado = models.BooleanField(default=False)

class Wishlist(models.Model):
    nome_evento = models.CharField(max_length=100) #forms
    data_evento = models.DateField(blank=True, null=True) #forms
    foi_paga = models.BooleanField(default=False)
    valida = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    creditos_colocados = models.DecimalField(max_digits=10, decimal_places=0)
    link_musica = models.URLField(blank=True, null=True) #forms
    comprado_por = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, null=True, blank=True)
    horario_evento = models.TimeField(blank=True, null=True) #forms
    descricao_evento = models.TextField(blank=True, null=True) #forms
    itens = models.ManyToManyField(Item, blank=True)

class PlanoCredito(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=10, decimal_places=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)