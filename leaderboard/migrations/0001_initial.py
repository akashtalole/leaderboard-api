# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-02 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('rank', models.IntegerField(default=0)),
                ('kills', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('submission_date', models.DateTimeField()),
                ('game', models.CharField(max_length=50)),
            ],
        ),
    ]
