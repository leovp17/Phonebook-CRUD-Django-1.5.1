from django.conf.urls import patterns, url

from MultipleInlineFormset import views
from .views import BandCreate, BandList, BandDetail, BandUpdate, BandDelete

urlpatterns = patterns('',
                       #ex: /mif/index or /mif/
                       url(r'^band/add/$', BandCreate.as_view(), name="band_add"),
                       url(r'^band/list/$', BandList.as_view(), name="band_list"),
                       url(r'^band/detail/(?P<pk>[\d-]+)/$', BandDetail.as_view(), name="band_detail"),
                       url(r'^band/update/(?P<pk>[\d-]+)/$', BandUpdate.as_view(), name="band_update"),
                       url(r'^band/delete/(?P<pk>[\d-]+)/$', BandDelete.as_view(), name="band_delete"),
)
