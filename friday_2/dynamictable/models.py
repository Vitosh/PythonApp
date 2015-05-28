from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    tname = models.TextField(blank=True, null=True,unique = True)

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.__str__()


class Label(models.Model):
    tname = models.ForeignKey(Table, blank=True, null=True)
    column = models.TextField(blank=True, null=True)
    txt = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.movie + " " + self.episode

    def __repr__(self):
        return self.__str__()
