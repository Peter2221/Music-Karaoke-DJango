from django.urls import path
from . import views

app_name = 'songs'
urlpatterns = [
  # /songs
  path('', views.index, name="index"),
  # songs/<id>
  path('<int:song_id>/', views.show_details, name="show_details")
]