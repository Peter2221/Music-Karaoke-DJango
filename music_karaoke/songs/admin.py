from django.contrib import admin

from .models import Song
from authentication.models import UserFavouriteSong
from authentication.models import Ranking


admin.site.register(Song)
admin.site.register(UserFavouriteSong)
admin.site.register(Ranking)
