from django.core.management.base import BaseCommand
from wishlists.models import PlanoCredito


class Command(BaseCommand):
    help = 'Cria dois planos de crédito'

    def handle(self, *args, **kwargs):
        # Plano 1
        plano1 = PlanoCredito.objects.create(
            nome='Plano Básico',
            quantidade=1,
            preco=19.99,
            descricao='Plano Básico de créditos'
        )

        # Plano 2
        plano2 = PlanoCredito.objects.create(
            nome='Plano Profissional',
            quantidade=3,
            preco=39.99,
            descricao='Plano Profissional com mais créditos'
        )

        # Exibe uma mensagem ao final
        self.stdout.write(self.style.SUCCESS(f'Planos criados com sucesso: {plano1.nome}, {plano2.nome}'))
