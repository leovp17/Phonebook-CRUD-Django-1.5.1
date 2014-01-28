#urls.py

from django.conf.urls import url, patterns
from inlines.views import candidato_details

urlpatterns = patterns('',
    url(r'^candidate/(?P<slug>[^\.]+).html' , candidato_details,name="candidato_detail"),
)