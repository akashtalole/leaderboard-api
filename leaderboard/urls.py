from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/(?P<username>[a-z-A-Z0-9]{5,16})/(?P<game>[a-zA-Z0-9]{1,50})/(?P<score>[0-9]{1,10})/(?P<kills>[0-9]{1,10})/$', views.submit_score, name="submit score"),
    url(r'^LeaderBoard$', views.by_match_time, name="leaderboard by match and time"),
    url(r'^LeaderBoard/:id$', views.by_matchname, name="leaderboard by match name"),
    url(r'^playersStats/:id$', views.playerstats, name="player stats"),
    url(r'^playersStats$', views.playerstats_match, name="player stats by match"),

    ]
