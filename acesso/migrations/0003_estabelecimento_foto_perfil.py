# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0002_auto_20170428_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='estabelecimentos', verbose_name='Perfil'),
        ),
    ]