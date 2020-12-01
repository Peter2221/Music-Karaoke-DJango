from django.contrib import admin

from .models import Song
from .models import UserFavouriteSong
from .models import Ranking


admin.site.register(Song)
admin.site.register(UserFavouriteSong)
admin.site.register(Ranking)
