from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from vdrinking.bmi.models import Game
from vdrinking.bmi.models import MyGame, MyGameForm
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from vdrinking.bmi.models import ContactForm
from django.contrib.auth import logout

def home(request):
    if request.user.is_authenticated():     
        warning = "You are logged in. Yay!"
        games = Game.objects.all()
        auth = True        
        latestgames = Game.objects.order_by('name')[:5]
    else:
        warning = "You are not logged in. Boo!"
        games = []
        auth = False
        latestgames = Game.objects.order_by('name')[:5]
    return render_to_response('home.html', {
    'games': games, 
    'warning': warning,
    'auth': auth,
    'latestgames': latestgames, 
     }, context_instance=RequestContext(request))

@csrf_protect

def detail(request, game_id): 
    if request.method == 'POST': # If the form has been submitted...
        form = MyGameForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('') # Redirect after POST
    else:
        game = Game.objects.get(id=game_id)
        form = MyGameForm() # An unbound form

    return render_to_response('glee.html', {
        'form': form,
        'game': game, 
    }, context_instance=RequestContext(request))

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

@login_required
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    games = MyGame.objects.filter(user=user)
    return render_to_response('profile.html', {
    'games': games, 
    'user': user, 
    })

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })

def logout(request):
    bye = "You are now logged out!"
    return render_to_response('logout.html', {
        'bye': bye,
    })
