from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view='example.views.index',
        name='project.home'
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(r'^home/user/$',
        view=RedirectView.as_view(url=reverse_lazy('base.comment')),
        name='project.home.user'
        ),
    url(regex=r'^base/',
        view=include('base.urls')
        ),
)

urlpatterns += staticfiles_urlpatterns()
