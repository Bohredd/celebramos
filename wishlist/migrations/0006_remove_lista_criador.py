# Generated by Django 5.1.1 on 2024-10-10 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0005_lista_criador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='criador',
        ),
    ]
