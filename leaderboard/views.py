# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Player, Game

# Create your views here.
def index(reqest):
    to_ret = {"username": "test", "rank": 10, "kills": 10, "score": 200}
    return JsonResponse(to_ret, content_type='application/json')

def submit_score(reqest, username, score, kills, game):
    to_ret = {"username": username, "rank": 10, "kills": kills, "score": score, "games":game}
    p = Player(username=username, kills=kills, score=score, games=game)
    p.save()
    return JsonResponse(to_ret, content_type='application/json')
