# Generated by Django 5.1.1 on 2024-10-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0002_alter_wishlist_data_evento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='creditos_colocados',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
