from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


def post_list(request, pk=User):
    posts = Post.objects.filter(author_id=request.user.id)
    user_info = User.objects.all()
    return render(request, 'blog/post_list.html',  {'posts': posts, "user_info": user_info})


def post_detail(request,    pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',    {'post':    post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',  {'form':    form})


def post_edit(request,  pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,  instance=post)
        if "delete" in request.POST:
            print("delete hit")
            post.delete()

        else:
            print("save hit")
            if form.is_valid():
                if (post.status):
                    post.published_date = timezone.now()
                else:
                    post.published_date = None
                post = form.save(commit=False)
                post.author = request.user
                post.save()

        return redirect('blog.views.post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html',  {'form': form})
