from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^home$', views.home, name="home"),  
    url(r'^ourStory$', views.our_story, name="our_story"),
    url(r'^clubs$', views.testingClub, name="testingClub"),   
    url(r'^competitions$', views.testingCompetition, name="testingCompetition"),   
    url(r'^majors$', views.testingMajor, name="testingMajor"),   
    url(r'^competitions/(?P<pk>\d+)/$', views.competition_individual, name="competition_individual"),
    url(r'^clubs/(?P<pk>\d+)/$', views.club_individual, name="club_individual"),
    url(r'^majors/(?P<pk>\d+)/$', views.major_individual, name="major_individual"),


]