# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rushi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushi',
            name='age',
            field=models.IntegerField(),
        ),
    ]
