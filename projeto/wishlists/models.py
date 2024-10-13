from django.db import models

class Item(models.Model):
    nome_item = models.CharField(max_length=100)
    link_compra = models.URLField()
    comprado = models.BooleanField(default=False)

class Wishlist(models.Model):
    nome_evento = models.CharField(max_length=100)
    data_evento = models.DateField()
    foi_paga = models.BooleanField(default=False)
    valida = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    creditos_colocados = models.DecimalField(max_digits=10, decimal_places=2)
    link_musica = models.URLField()
