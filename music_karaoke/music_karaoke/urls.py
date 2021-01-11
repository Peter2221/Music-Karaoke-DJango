"""music_karaoke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication import views as views_auth
from django.contrib.auth import views as auth_views
from songs import views as views_song
from analysis import views as views_analysis
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('register', views_auth.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    path('login', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    path('', include("django.contrib.auth.urls")),
    path('', views_song.landing, name="landing"),
    path('', include("authentication.urls")),
    path('songs', include('songs.urls')),
    path('analysis', include('analysis.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
