from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from .models import Ranking


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            profile_form = ProfileForm(request.POST, request.FILES)
            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.profile_pic.name = '{}.jpg'.format(user.id)
                profile.save()
                return redirect("/")
        else:
            form = RegisterForm()
            profile_form = ProfileForm()
        return render(request, "register.html", {"form": form, "profile_form": profile_form})


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
