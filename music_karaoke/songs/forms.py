
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title" , "author", "genre", "audio_file", "song_image"]