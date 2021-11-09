from django.urls import path

from realmadrid import views

urlpatterns=[
    path('', views.jugadores, name='jugadores'),

]