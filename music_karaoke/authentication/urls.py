from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    path('ranking', views.show_ranking, name="ranking")
]
