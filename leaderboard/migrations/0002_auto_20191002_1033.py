# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-02 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
                ('kills', models.IntegerField()),
                ('score', models.IntegerField()),
                ('submission_date', models.DateTimeField()),
                ('games', models.ManyToManyField(blank=True, to='leaderboard.Game')),
            ],
        ),
        migrations.DeleteModel(
            name='Leaderboard',
        ),
    ]
