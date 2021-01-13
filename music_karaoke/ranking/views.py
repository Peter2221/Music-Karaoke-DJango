from django.shortcuts import render
from .models import Ranking

# Create your views here.
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