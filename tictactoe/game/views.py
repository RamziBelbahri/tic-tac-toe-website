from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Player, Game


def index(request):
    return HttpResponse("play game:")


def game(request, game_id):
    game_size = get_object_or_404(Game, pk=game_id).size
    context = {'game_size': range(0, game_size)}

    if request.POST.get('click', False):
        print("hi")

    return render(request, 'game/game.html', context)
# Create your views here.
