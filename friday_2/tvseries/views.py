from django.shortcuts import render
from tvseries import models
from django.contrib.auth.models import User


def add_to_db(movie, episode, season, user, watched=False):
    q = models.Series(
        movie=movie, episode=episode, user=user, season=season, watched=watched)
    q.save()


def delete_e(target):
    del_me = models.Series.objects.filter(id=target)
    del_me.delete()


def update_me(movie, episode, season, is_watched):
    if is_watched is not None:
        to_upd = models.Series.objects.select_for_update().filter(
            movie=movie, episode=episode,season =season).update(watched=is_watched)


# Create your views here.


def index(request):

    tv = models.Series.objects.all().order_by("id")
    user = request.user

    if request.method == "POST":
        movie = request.POST.get("movie")
        season = request.POST.get("season")
        episode = request.POST.get("episode")
        watched = request.POST.get("watched")

        if watched is None:
            watched = 0

        if episode in str(tv) and movie in str(tv):
            update_me(movie, episode, season, user, int(watched))
        else:
            add_to_db(movie, episode, season, user, int(watched))

    if request.method == "GET":
        target = request.GET.get("target")
        delete_e(target)

    #update_me("rado", "1", 1)

    return render(request, "tv.html", locals())
