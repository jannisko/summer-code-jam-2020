from django.db import models

# Create your models here.

class gameSession(models.Model):
    gameId = models.CharField(max_length=255, blank=True, null=True)

class gameMoves(models.Model):
    game = models.ForeignKey(gameSession, on_delete=models.CASCADE)
    enemyMoves = models.TextField(default="       -       -       -       -       ")
    playerMoves = models.TextField(default="       -       -       -       -       ")
    enemyShots = models.TextField(default="")
    playerShots = models.TextField(default="")
