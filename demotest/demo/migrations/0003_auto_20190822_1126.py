# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-08-22 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20190810_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='AD',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'test2',
            },
        ),
        migrations.CreateModel(
            name='Many',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'many',
            },
        ),
        migrations.CreateModel(
            name='One',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'one',
            },
        ),
        migrations.AddField(
            model_name='many',
            name='fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.One'),
        ),
    ]
