from django.core.management.base import BaseCommand
from wishlist.models import TipoWishlist

class Command(BaseCommand):
    help = 'Cria tipos de Wishlist no banco de dados'

    def handle(self, *args, **kwargs):
        TipoWishlist.objects.create(
            nome="Basico",
            maximo_fotos_site=1,
            reutilizavel=False,
            tempo_online_site=3,
            has_musica_site=False,
            maximo_reutilizacao_sites=1,
            preco_tipo=19.99
        )
        TipoWishlist.objects.create(
            nome="Profissional",
            maximo_fotos_site=3,
            reutilizavel=True,
            tempo_online_site=12,
            has_musica_site=True,
            maximo_reutilizacao_sites=3,
            preco_tipo=49.99
        )

        self.stdout.write(self.style.SUCCESS('Tipos de Wishlist criados com sucesso!'))
