from django.db import models

# Create your models here.

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class Player(models.Model):
    name = models.CharField(max_length=32)