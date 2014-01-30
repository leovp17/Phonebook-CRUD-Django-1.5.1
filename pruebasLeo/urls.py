from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from inlines.views import enter_edu, show_edu
from micrud.views import enter
from recipes.views import enterRecipe

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebasLeo.views.home', name='home'),
    # url(r'^pruebasLeo/', include('pruebasLeo.foo.urls')),

    url(r'^micrud/', include('micrud.urls', namespace="micrud")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^recipes/', include('recipes.urls', namespace="recipes")),
    url(r'^extraviews/', include('extra_views.tests.urls', namespace="extraviews")),
    url(r'^inlines/', include('inlines.urls', namespace="inlines")),
    url(r'^mif/', include('MultipleInlineFormset.urls', namespace="mif")),
    #url(r'^musicapi/',include('musicapi.urls',namespace='musicapi')),
    url(r'^forminline/', include('forminline.urls', namespace="forminline")),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^enter/', enter),
    url(r'^enterRecipe/', enterRecipe),

    url(r'^enter_edu/', enter_edu),
    url(r'^show_edu/', show_edu),
)