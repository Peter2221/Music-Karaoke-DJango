from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import SongForm
from .models import Song
from authentication.models import UserFavouriteSong


def landing(request):
    return render(request, 'landing-page/landing.html')


# Create your views here.
def index(request):
    songs = Song.objects.all()
    return render(request, 'song_index.html', {'songs': songs})


def show_details(request, song_id):
    song = Song.objects.get(id=song_id)
    favourite = UserFavouriteSong.objects.filter(song = song).count()
    return render(request, 'details.html', {'song': song, 'favourite':favourite})

def show_favourites(request):
    songs = []
    favourite_songs = UserFavouriteSong.objects.filter(user = request.user).values()
    for favourite_song in favourite_songs:
        songs.append(Song.objects.get(id=favourite_song['song_id']))
    return render(request, 'song_index.html', {'songs' : songs})

def add_song_to_favourites(request, song_id):
    favourite_song = UserFavouriteSong()
    favourite_song.user = request.user
    favourite_song.song = Song.objects.get(id=song_id)
    favourite_song.save()
    return redirect('../{}'.format(song_id))



@permission_required('is_superuser', login_url='/')
def add_new_song(request):
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SongForm()
    return render(request, "add_song.html", {"form": form})
