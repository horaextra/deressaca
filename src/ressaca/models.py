from django.db import models

class Hangovers(models.Model):

    day = DateField(required=True)
    counter = IntegerField(required = True)
