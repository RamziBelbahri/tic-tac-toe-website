from django.urls import path

from .views import *


app_name = 'game'
urlpatterns = [
    path('home', index, name='index'),
    path('<int:game_id>', GameView.game, name='currentGame'),
]
