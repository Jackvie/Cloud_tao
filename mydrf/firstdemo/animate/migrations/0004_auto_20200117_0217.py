# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-17 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animate', '0003_auto_20200117_0214'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='imagebase',
            name='chapter_name',
        ),
    ]