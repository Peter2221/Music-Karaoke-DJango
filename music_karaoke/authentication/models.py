from django.db import models
from django.contrib.auth.models import User
from songs.models import Song


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, upload_to="media/images")


class UserFavouriteSong(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    song = models.ForeignKey(to=Song, on_delete=models.CASCADE)


class Ranking(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    song = models.ForeignKey(to=Song, on_delete=models.CASCADE)
    score = models.IntegerField()
    datetime = models.DateTimeField()
