# _*_ coding:utf-8_*_

from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('pacientes.views',

                       url(r'^$', 'listar', name='listar_pacientes'),
                       url(r'^exportar$', 'exportar', name='exportar_pacientes'),
                       url(r'^(?P<id>\d+)/$', 'consultar', name='consultar_paciente'),
                       url(r'^incluir/$', 'incluir', name='incluir_paciente'),
                       url(r'^editar/(?P<id>\d+)/$', 'editar', name='editar_paciente'),
                       url(r'^inativar/(?P<id>\d+)/$', 'inativar', name='inativar_paciente'),
                       url(r'^excluir/(?P<id>\d+)/$', 'excluir', name='excluir_paciente'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            (r'media/(?P<path>.*)$', 'serve'),
    )
