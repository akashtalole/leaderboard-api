# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    games = models.ManyToManyField('Game', blank=True)
    submission_date = models.DateTimeField()

    def __str__(self):
        return self.username

class Game(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
