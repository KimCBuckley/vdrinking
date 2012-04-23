from django.db import models 
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def get_absolute_url(self): 
        return "/bmi/%i/" % self.id
    def __unicode__(self):
        return self.name

class MyGame(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)
    final_bac = models.FloatField()
    def __unicode__(self):
        return self.game.name

class MyGameForm(ModelForm):
    class Meta:
        model = MyGame

class User(models.Model): 
    user = User
    games = MyGame.objects.filter(user=User)
    def __unicode__(self):
        return self.name

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
