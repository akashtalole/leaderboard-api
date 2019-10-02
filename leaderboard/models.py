# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Player(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    submission_date = models.DateTimeField()
    game = models.CharField(max_length=50)

    def __str__(self):
        return self.username

