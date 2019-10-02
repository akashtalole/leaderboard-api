# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Player
from datetime import datetime
from pytz import UTC

# Create your views here.
def by_match_time(request):
    match = request.GET['match']
    time = request.GET['time']
    res = Player.objects.filter(game=match)
    print res
    to_ret = {"username": "test", "rank": 10, "kills": 10, "score": 200}
    return JsonResponse(to_ret, content_type='application/json')

def submit_score(request, username, score, kills, game):
    to_ret = {"username": username, "rank": 10, "kills": kills, "score": score, "games":game}
    submission_date = datetime.now()
    p = Player(username=username, kills=kills, score=score, game=game, submission_date=submission_date)
    p.save()
    return JsonResponse(to_ret, content_type='application/json')

def by_matchname(request):
    match = request.GET['match']
    res = Player.objects.filter(game=match)
    return JsonResponse(serializers.serialize('json', res), content_type='application/json', safe=False)

def playerstats(request):
    match =''
    res = Player.objects.filter(game=match)
    print res
    to_ret = {"username": "test", "rank": 10, "kills": 10, "score": 200}
    return JsonResponse(to_ret, content_type='application/json')

def playerstats_match(request):
    match = request.GET['match']
    res = Player.objects.filter(game=match)
    return JsonResponse(serializers.serialize('json', res), content_type='application/json', safe=False)
