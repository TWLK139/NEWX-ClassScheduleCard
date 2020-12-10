from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('login', views.login),
    path('kick', views.kick),
    path('logout', views.logout),
    path('schedule', views.schedule),
    path('getschedule', views.getschedule),
    path('score', views.score),
    path('exam', views.exam),
    path('info', views.info),
    path('edit', views.edit),
    path('now', views.now),
    path('datas', views.normaldatas),
    path('getapplystatus', views.getapplystatus),
    path('setapplystatus', views.setapplystatus),
    path('scodes', views.scodes),
    path('getrecords', views.getrecords),
]