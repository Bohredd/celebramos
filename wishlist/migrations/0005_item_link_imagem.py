# Generated by Django 5.1.1 on 2024-10-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_remove_site_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='link_imagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]
