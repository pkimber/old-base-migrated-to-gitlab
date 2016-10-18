# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import HomeView


admin.autodiscover()


urlpatterns = [
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^',
        view=include('login.urls')
        ),
]

urlpatterns += staticfiles_urlpatterns()
