from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):

    name = models.TextField(null=True, blank=True)
    sound = models.TextField(null=True, blank=True)

    def speak(self):
        return 'The '+self.name+' says "'+self.sound+'"'


class Task(models.Model):

    name = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)