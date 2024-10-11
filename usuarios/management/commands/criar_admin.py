from django.core.management.base import BaseCommand
from usuarios.models import Usuario
from decouple import config
class Command(BaseCommand):
    help = 'Cria um usuário administrador com o e-mail admin@bohredd.dev'

    def handle(self, *args, **kwargs):
        email = config("ADMIN_EMAIL")
        nome_completo = 'Admin Sistema'
        senha = config("ADMIN_PASSWORD")

        if not Usuario.objects.filter(email=email).exists():
            Usuario.objects.create_superuser(
                email=email,
                nome_completo=nome_completo,
                password=senha
            )
            self.stdout.write(self.style.SUCCESS(f'Usuário admin ({email}) criado com sucesso!'))
        else:
            self.stdout.write(self.style.WARNING(f'Usuário com o e-mail {email} já existe.'))
