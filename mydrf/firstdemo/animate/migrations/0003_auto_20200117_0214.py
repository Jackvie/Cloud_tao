# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-17 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animate', '0002_auto_20200116_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagebase',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterIndexTogether(
            name='imagebase',
            index_together=set([]),
        ),
        migrations.AddIndex(
            model_name='imagebase',
            index=models.Index(fields=['chapter', 'name'], name='chapter_name'),
        ),
        migrations.RemoveField(
            model_name='imagebase',
            name='page_number',
        ),
    ]