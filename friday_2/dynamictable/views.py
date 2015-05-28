from django.shortcuts import render
from dynamictable import models
from django.db import IntegrityError


def add_new_table(tname, user):
    q = models.Table(tname=tname, user=user)
    q.save()
    return q


def add_label(t_id, col, user, text):
    q = models.Label(tname=t_id, txt=text, user=user, column=col)
    q.save()


def get_table_id(name):
    return models.Table.objects.filter(tname=name).get()


def get_models():
    return (models.Table.objects.all(), models.Label.objects.all())


# Create your views here.


def index(request):
    user = request.user

    if request.method == "POST":
        name = request.POST.get("name")

        try:
            t_id = add_new_table(name, user)
        except IntegrityError:
            t_id = get_table_id(name, user)

        col = request.POST.get("column")
        txt = request.POST.get("txt")
        add_label(t_id, col, user, txt)

    return render(request, "dt.html", locals())


def table(request):
    table, columns = get_models()
    print(columns)
    return render(request, "table.html", locals())
