from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Player, Game
from django.views.generic import View




def index(request):
        # html = render_to_string('mysite/sidebar_trend.html', {'form': form})
        """form = form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return render(request, 'game/home.html')"""
        print(request)
        return render(request, 'game/home.html')
    
class GameView(View):

    def game(request, game_id):
        game_size = get_object_or_404(Game, pk=game_id).size
        context = {'game_size': range(0, game_size)}

        if request.POST.get('click', False):
            print("hi")

        return render(request, 'game/game.html', context)
    # Create your views here.

    def sayHi(request):
        print("hi")
        
    def gameEnd(request, result):
        if request.method == "POST":
            print("hi")
            return render(request, 'game/game.html')
        