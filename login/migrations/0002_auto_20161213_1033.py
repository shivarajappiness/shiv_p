# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puser',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
    ]
