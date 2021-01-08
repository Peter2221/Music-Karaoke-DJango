from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm

# Create your views here.
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

