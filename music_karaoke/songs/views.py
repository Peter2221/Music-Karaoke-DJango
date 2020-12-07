from django.shortcuts import render, redirect

def landing(request):
    return render(request, 'landing-page/landing.html')

# Create your views here.
def index(request):
    songs = [
        {'id': 1, 'title': 'Boyfriend', 'artist': 'Justin Bieber', 'genre': 'pop', 'url': 'https://cdn.pixabay.com/photo/2020/11/25/14/37/portrait-5775938_960_720.jpg'},
        {'id': 2, 'title': 'Boyfriend', 'artist': 'Justin Bieber', 'genre': 'pop', 'url': 'https://cdn.pixabay.com/photo/2020/11/25/14/37/portrait-5775938_960_720.jpg'},
        {'id': 3, 'title': 'Boyfriend', 'artist': 'Justin Bieber', 'genre': 'pop', 'url': 'https://cdn.pixabay.com/photo/2020/11/25/14/37/portrait-5775938_960_720.jpg'},
    ]
    return render(request, 'songs/index.html', {'songs' : songs})

def show_details(request, song_id):
    song = {'title': 'Boyfriend', 'artist': 'Justin Bieber', 'genre': 'pop', 'url': 'https://cdn.pixabay.com/photo/2020/11/25/14/37/portrait-5775938_960_720.jpg'}
    return render(request, 'songs/details.html', {'song' : song})

