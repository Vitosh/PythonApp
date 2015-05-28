from django.db import models
from django.contrib.auth.models import User


class Series(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    movie = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    episode = models.TextField(blank=True, null=True)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.movie + " " + self.episode

    def __repr__(self):
        return self.__str__()
