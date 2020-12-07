from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    audio_file = models.FileField(blank=False, default = "", upload_to="media/audio_files")
    song_image = models.ImageField(blank= False, default = "" , upload_to = "media/song_images")
