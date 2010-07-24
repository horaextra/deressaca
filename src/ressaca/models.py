from django.db import models

class Hangovers(models.Model):

    day = models.DateField()
    counter = models.IntegerField()
