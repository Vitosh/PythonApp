"""dbmagic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import tvseries.views
import dbapp.views
import dynamictable.views
import todo.views

urlpatterns = [
    url(r'^post/new/$', todo.views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/blog.views.post_list$',
        todo.views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$',  todo.views.post_detail),
    url(r'^post/(?P<pk>[0-9]+)/edit/blog.views.post_list$',
        todo.views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',
        todo.views.post_edit, name='post_edit'),
    url(r'^post/new/blog.views.post_list$', todo.views.post_list),
    url(r"^todo/", todo.views.post_list, name="todo"),
    url(r"^tables/", dynamictable.views.table, name="tables"),
    url(r"^dtable/", dynamictable.views.index, name="dt"),
    url(r"^register/", dbapp.views.register, name="register"),
    url(r"^main/", dbapp.views.main, name="main"),
    url(r"^$", dbapp.views.index, name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tvseries/$', tvseries.views.index, name="tvseries"),
    url(r"^logout/$", dbapp.views.main_logout, name="logout"),
    url(r"^todo/", dbapp.views.todo, name="todo"),
    url(r"^groceries/", dbapp.views.todo, name="groceries"),
]
