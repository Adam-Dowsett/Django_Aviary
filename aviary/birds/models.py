from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Bird(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.name} is a {self.species.name} and is {self.age} years old. {self.species.description}"