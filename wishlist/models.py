from django.db import models

class Site(models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField()
    slug = models.SlugField(max_length=100, unique=True)
    pago = models.BooleanField(default=False)
    comprador = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    lista = models.ForeignKey('Lista', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Lista(models.Model):
    nome = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item)

    def __str__(self):
        return self.nome