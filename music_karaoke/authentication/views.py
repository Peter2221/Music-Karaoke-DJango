from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        profile_form = ProfileForm(response.POST, response.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("/")
    else:
        form = RegisterForm()
        profile_form = ProfileForm()
    return render(response, "registration/register.html", {"form":form, "profile_form":profile_form})

