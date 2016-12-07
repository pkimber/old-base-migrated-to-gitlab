# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import (
    HomeView,
    DashView,
    SettingsView,
    FileDropDemoView,
    AjaxFileUploadView,
)

admin.autodiscover()


urlpatterns = [
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
    url(regex=r'^dash/$',
        view=DashView.as_view(),
        name='project.dash'
        ),
    url(regex=r'^settings/',
        view=SettingsView.as_view(),
        name='project.settings'
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^dash/filedrop/',
        view=FileDropDemoView.as_view(),
        name='filedrop.demo',
        ),
    url(regex=r'^ajax-upload/$',
        view=AjaxFileUploadView.as_view(),
        name='ajax.file.upload',
        ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
