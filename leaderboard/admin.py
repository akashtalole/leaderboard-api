# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['username', 'rank', 'kills', 'score']

