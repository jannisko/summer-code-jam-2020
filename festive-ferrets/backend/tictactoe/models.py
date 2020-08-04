from django.db import models

# Create your models here.

class liveGame(models.Model):
    gameId = models.CharField(max_length=255, blank=True, null=True)


class gameMoves(models.Model):
    game = models.ForeignKey(liveGame, on_delete=models.CASCADE)
    moves = models.TextField(default='         ')
    player = models.CharField(max_length=1,default="O")
