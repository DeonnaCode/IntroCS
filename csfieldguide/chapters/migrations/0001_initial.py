# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('other_resources', models.TextField(null=True)),
                ('icon', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
