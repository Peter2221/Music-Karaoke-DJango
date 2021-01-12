from django.urls import path
from . import views

app_name = 'songs'
urlpatterns = [
    # /songs
    path('', views.index, name="index"),
    # songs/<id>
    path('/<int:song_id>', views.show_details, name="show_details"),
    # songs/AddSong
    path('/AddSong', views.add_new_song, name="add_new_song"),
    # songs/<id>/add_to_favourite
    path('/<int:song_id>/add_to_favourite', views.add_song_to_favourites, name="add_to_favourite"),
    # songs/favourites
    path('/favourites', views.show_favourites, name="show_favourites"),
]
