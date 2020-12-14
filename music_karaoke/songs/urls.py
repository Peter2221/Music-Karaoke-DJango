from django.urls import path
from . import views

app_name = 'songs'
urlpatterns = [
  # /songs
  path('', views.index, name="index"),
  # songs/<id>
  path('/<int:song_id>', views.show_details, name="show_details"),
  # songs/AddSong
  path('/AddSong', views.add_new_song, name="add_new_song")
]