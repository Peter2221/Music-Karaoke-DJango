from django.db import models
from songs.models import Song
from authentication.models import Profile

class Ranking(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    song = models.ForeignKey(to=Song, on_delete=models.CASCADE)
    score = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)