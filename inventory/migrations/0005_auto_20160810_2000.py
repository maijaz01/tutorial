# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20160810_1954'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='Inventory',
        ),
    ]
