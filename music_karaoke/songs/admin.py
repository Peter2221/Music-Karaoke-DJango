from django.contrib import admin

from .models import Song
from authentication.models import UserFavouriteSong



admin.site.register(Song)
admin.site.register(UserFavouriteSong)

