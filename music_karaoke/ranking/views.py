from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ranking.models import Ranking
from authentication.models import Profile
from songs.models import Song


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


@csrf_exempt
def save_rank(request):
    if request.method == "POST":
        score = request.POST.get('score')
        song_id = request.POST.get('song_id')
        user_id = request.user.id
        save_in_database(user_id, song_id, score)
        return JsonResponse({'status': 200})


def save_in_database(user_id, song_id, score):
    rank = Ranking()
    rank.profile = Profile.objects.get(id=user_id)
    rank.song = Song.objects.get(id=song_id)
    rank.score = score
    rank.save()
