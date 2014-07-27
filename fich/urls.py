# _*_ coding:utf-8 _*_

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'home.views.home', name='home'),
                       url(r'^paciente/', include('pacientes.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            (r'media/(?P<path>.*)$', 'serve'),
    )