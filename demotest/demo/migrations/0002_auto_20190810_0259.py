# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-10 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jd',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
