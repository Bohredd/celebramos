# Generated by Django 5.1.1 on 2024-10-12 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0005_item_link_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
