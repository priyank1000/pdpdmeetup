# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-14 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
