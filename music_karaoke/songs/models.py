from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)


class UserFavouriteSong(models.Model):
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    id_song = models.ForeignKey(to=Song, on_delete=models.CASCADE)


class Ranking(models.Model):
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    id_song = models.ForeignKey(to=Song, on_delete=models.CASCADE)
    score = models.IntegerField()
    datetime = models.DateTimeField()

