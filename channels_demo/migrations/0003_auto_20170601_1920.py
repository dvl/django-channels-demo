# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels_demo', '0002_lote_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lance',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]