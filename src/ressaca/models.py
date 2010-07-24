from django.db import models

class Hangover(models.Model):

    day = models.DateField(auto_now=True)
