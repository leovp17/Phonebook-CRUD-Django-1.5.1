#urls.py
from django.conf.urls import patterns, url, include
from recipes.views import RecetaList, RecetaDetail, RecetaCreateView, \
    RecetaUpdateView, RecetaCreateNamedView, RecetaUpdateNamedView

urlpatterns = patterns('',
    url(r'^$', RecetaList.as_view(), name='RecetaList'),
    url(r'^RecetaCreate/$', RecetaCreateView.as_view(), name='RecetaCreate'),
    url(r'^RecetaCreateNamed/$', RecetaCreateNamedView.as_view(), name='RecetaCreateNamed'),
    url(r'^RecetaUpdate/(?P<slug>[\w-]+)/$', RecetaUpdateView.as_view(), name='RecetaUpdate'),
    url(r'^RecetaUpdateNamed/(?P<slug>[\w-]+)/$', RecetaUpdateNamedView.as_view(), name='RecetaUpdateNamed'),
    url(r'^RecetaDetail/(?P<slug>[\w-]+)/$', RecetaDetail, name='RecetaDetail')
)