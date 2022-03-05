from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
# from .models import Player, Game
from django.views.generic import View


def index(request):
    return HttpResponse("play game:")

"""class GameView(View):

    def home(request, game_id):
        # game_size = get_object_or_404(Game, pk=game_id).size
        #context = {'game_size': range(0, game_size)}

        if request.POST.get('click', False):
            print("hi")

        return render('game/game.html')
    # Create your views here."""