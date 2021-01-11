from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import SongForm
from .models import Song
from authentication.models import Ranking, Profile


def landing(request):
    return render(request, 'landing-page/landing.html')


# Create your views here.
def index(request):
    songs = Song.objects.all()
    return render(request, 'song_index.html', {'songs': songs})


def show_details(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'details.html', {'song': song})


def add_song_to_favourites(request, song_id):
    pass


def show_ranking(request):
    ranking = Ranking.objects.order_by('score').reverse().all()
    position_count = 0
    for rank in ranking:
        rank = fill_ranking_object(rank)
        position_count += 1
        rank.position_count = position_count
    return render(request, 'ranking.html', {'ranking': ranking})


def fill_ranking_object(rank):
    profile = rank.profile
    user = profile.user
    rank.profile_pic = profile.profile_pic
    rank.first_name = user.first_name
    rank.last_name = user.last_name
    rank.song = rank.song
    return rank


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
