# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-10 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citas',
            options={'verbose_name': 'Cita', 'verbose_name_plural': 'Cita'},
        ),
        migrations.AlterField(
            model_name='citas',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]