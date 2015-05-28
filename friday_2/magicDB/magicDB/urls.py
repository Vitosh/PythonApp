from django.conf.urls import include, url
from django.contrib import admin

from db_app import urls as db_app_urls

urlpatterns = [

    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'', include(db_app_urls)),
]
