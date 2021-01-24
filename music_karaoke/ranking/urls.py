from django.urls import path
from . import views

app_name = 'ranking'
urlpatterns = [
    path('', views.show_ranking, name="index"),
    path('/save', views.save_rank, name="save_rank")
]
