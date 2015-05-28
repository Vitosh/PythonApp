from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todo.models import Post


def main_logout(request):
    logout(request)
    return redirect("index")


def index(request):
    if request.user.is_authenticated():
        return redirect("main")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return redirect("index")

    else:
        return render(request, "index.html", locals())


@login_required(login_url="index")
def main(request):
    username = request.user.username
    user_id = request.user.id
    total_tasks = Post.objects.all().filter(author_id=user_id)
    completed_tasks = Post.objects.all().filter(author_id=user_id, status=1)

    # print(username)
    # print(id)
    # print(total_tasks)
    # print(completed_tasks)

    # print(len(total_tasks))
    # print(len(completed_tasks))
    sum_total = len(total_tasks)
    sum_completed = len(completed_tasks)
    sum_pending = sum_total - sum_completed
    return render(request, "main.html", locals())


def todo(request):
    return render(request, "todo.html", locals())


def tvseries(request):
    return render(request, "tvseries.html", locals())


def _validate_register(username, email, password):
    if username is None or username.strip() == "":
        return False

    if email is None or email.strip() == "":
        return False

    if password is None or password.strip() == "":
        return False

    return True


def register(request):
    if request.user.is_authenticated():
        return redirect("main")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not _validate_register(username, email, password):
            return HttpResponseBadRequest("Something is missing")

        user = User.objects.create_user(username, email, password)
        return redirect("index")

    else:
        return render(request, "register.html", locals())
