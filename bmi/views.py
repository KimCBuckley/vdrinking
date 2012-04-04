from django.shortcuts import render_to_response

from vdrinking.bmi.models import Game

def home(request):    
    warning = "Warning, do not actually consume alcohol while playing this game online."
    games = Game.objects.all()
    return render_to_response('home.html', {
    'games': games, 
    'warning': warning,
    })

def detail(request, game_id): 
    game = Game.objects.get(id=game_id)
    return render_to_response('glee.html', {
    'game': game, 
    })
