# Generated by Django 5.1.1 on 2024-10-06 21:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('comprado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('itens', models.ManyToManyField(to='wishlist.item')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('pago', models.BooleanField(default=False)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishlist.lista')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishlist.site'),
        ),
    ]
