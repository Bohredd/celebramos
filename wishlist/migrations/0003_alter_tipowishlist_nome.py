# Generated by Django 5.1.1 on 2024-10-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_remove_site_lista_site_lista_ativa_site_listas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipowishlist',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
