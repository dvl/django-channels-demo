# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'ordering': ('-criado_em',),
                'get_latest_by': 'criado_em',
            },
        ),
        migrations.CreateModel(
            name='Leilao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('leilao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leilao.Leilao')),
            ],
        ),
        migrations.AddField(
            model_name='lance',
            name='lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leilao.Lote'),
        ),
        migrations.AddField(
            model_name='lance',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
