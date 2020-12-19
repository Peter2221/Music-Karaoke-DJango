from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import SongForm
from .models import Song

def landing(request):
    return render(request, 'landing-page/landing.html')

# Create your views here.
def index(request):
    '''
    songs = [
        {'id': 1, 'title': 'Boyfriend', 'artist': 'Justin Bieber', 'genre': 'pop', 'url': 'https://cdn.pixabay.com/photo/2020/11/25/14/37/portrait-5775938_960_720.jpg'},
        {'id': 2, 'title': 'Boyfriend', 'artist': 'Justin Bieber', 'genre': 'pop', 'url': 'https://cdn.pixabay.com/photo/2020/11/25/14/37/portrait-5775938_960_720.jpg'},
        {'id': 3, 'title': 'Boyfriend', 'artist': 'Justin Bieber', 'genre': 'pop', 'url': 'https://cdn.pixabay.com/photo/2020/11/25/14/37/portrait-5775938_960_720.jpg'},
    ]
    '''
    songs = Song.objects.all()
    return render(request, 'song_index.html', {'songs' : songs})

def show_details(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'details.html', {'song' : song})

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
