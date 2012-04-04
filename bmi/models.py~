from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    def get_absolute_url(self): 
        return "/bmi/%i/" % self.id
    def __unicode__(self):
        return self.name


