from django.db import models
# import what is below to add a user
from django.contrib.auth.models import User
# Create your models here.


class Word(models.Model):
    # setting user for authenticate 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    definition = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[0:50]



