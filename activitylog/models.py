from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField('date posted', auto_now=True)
    
    @classmethod
    def create(cls, name, type, description):
        activity = cls(name=name, type=type, description=description)
        return activity    