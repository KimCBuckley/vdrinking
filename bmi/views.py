from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from vdrinking.bmi.models import Game
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated():     
        warning = "You are logged in. Yay!"
        games = Game.objects.all()
        auth = True        
    else:
        warning = "You are not logged in. Boo!"
        games = []
        auth = False
    return render_to_response('home.html', {
    'games': games, 
    'warning': warning,
    'auth': auth,
    })

def detail(request, game_id): 
    game = Game.objects.get(id=game_id)
    return render_to_response('glee.html', {
    'game': game, 
    })

@csrf_protect
def create(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserCreationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/accounts/login/') # Redirect after POST
    else:
        form = UserCreationForm() # An unbound form

    return render_to_response('create.html', {
        'form': form,
    }, context_instance=RequestContext(request))
