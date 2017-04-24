# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewSharded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField()),
                ('review_string', models.CharField(max_length=120)),
            ],
        ),
    ]