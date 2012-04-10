from django.db import models 
from django.contrib.auth.models import User

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
    body_weight = models.IntegerField()    

