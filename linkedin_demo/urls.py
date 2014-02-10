#urls.py

from django.conf.urls import url, patterns
from .views import test1, response1, test2

urlpatterns = patterns('',
    url(r'^test1/$', test1, name="linkedin_test1"),
    url(r'^test2/(?P<slug>[\w-]+)', test2, name="linkedin_test2"),
    url(r'^response1/', response1, name="linkedin_response1")
)