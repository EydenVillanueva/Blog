# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.Publicacion')),
            ],
        ),
    ]
