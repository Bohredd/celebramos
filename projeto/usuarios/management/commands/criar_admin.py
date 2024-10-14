from django.core.management.base import BaseCommand
from decouple import config
from usuarios.models import Usuario

class Command(BaseCommand):
    help = 'Cria um usuário administrador usando variáveis de ambiente'

    def handle(self, *args, **kwargs):
        email = config('ADMIN_EMAIL')
        password = config('ADMIN_PASSWORD')

        if Usuario.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'Usuário administrador com o email {email} já existe.'))
            usuario = Usuario.objects.get(email=email)
            if usuario.is_superuser:
                usuario.set_password(password)
                usuario.save()
                self.stdout.write(self.style.WARNING('O usuário já é um superusuário.'))
            else:
                usuario.is_superuser = True
                usuario.save()
                usuario.set_password(password)
                self.stdout.write(self.style.SUCCESS('O usuário foi promovido a superusuário.'))
        else:
            Usuario.objects.create_superuser(
                email=email,
                password=password,
                nome_completo='Administrador',
            )
            self.stdout.write(self.style.SUCCESS(f'Usuário administrador criado com sucesso. Email: {email}'))
