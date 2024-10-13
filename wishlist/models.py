from django.db import models

class TipoWishlist(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    maximo_fotos_site = models.IntegerField()
    reutilizavel = models.BooleanField(default=False)
    tempo_online_site = models.IntegerField() # tempo em meses
    has_musica_site = models.BooleanField(default=False)
    maximo_reutilizacao_sites = models.IntegerField()
    preco_tipo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class Site(models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField()
    pago = models.BooleanField(default=False)
    comprador = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    listas = models.ManyToManyField('Lista')
    lista_ativa = models.ForeignKey('Lista', on_delete=models.CASCADE, related_name='lista_ativa', null=True, blank=True)
    tipo = models.ForeignKey('TipoWishlist', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=False)

    pode_reutilizar = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if self.id:
            quantia = self.listas.count()
            if quantia >= self.tipo.maximo_reutilizacao_sites:
                self.pode_reutilizar = False
            else:
                self.pode_reutilizar = True
        super().save(*args, force_insert, force_update, using, update_fields)

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    site = models.CharField(max_length=100, blank=True, null=True)
    comprado = models.BooleanField(default=False)
    link_imagem = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Lista(models.Model):
    nome = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item)

    def __str__(self):
        return self.nome