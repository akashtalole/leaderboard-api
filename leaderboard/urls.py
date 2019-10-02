from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/(?P<username>[a-z-A-Z0-9]{5,16})/(?P<game>[a-zA-Z0-9]{1,50})/(?P<score>[0-9]{1,10})/(?P<kills>[0-9]{1,10})/$', views.submit_score, name="submit score"),
    url(r'^LeaderBoard/', views.index, name="index"),
    ]
