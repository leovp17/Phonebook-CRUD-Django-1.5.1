#urls.py
from forminline.views import FormacionCreateView, FormacionList, NewFormacion, ViewFormacion
from django.conf.urls import patterns, url, include

__author__ = 'leovega'

formacion_urls = patterns('',
    url(r'^$', ViewFormacion.as_view(), name='formacion_detail'),
    #url(r'^Update$', EditPerson.as_view(), name='person_update'),
    #url(r'^Delete$', KillPerson.as_view(), name='person_delete'),
)

urlpatterns = patterns('forminline.views',
    url(r'^$', FormacionList.as_view(), name='formacion_list'),
    url(r'^add/$', FormacionCreateView.as_view(), name='formacion_add'),
    url(r'^agregar/$', NewFormacion.as_view(), name='formacion_agregar'),
    url(r'^(?P<slug>[\w-]+).estudio/', include(formacion_urls)),

)