#urls.py
from django.conf.urls import patterns, url, include
from recipes.views import RecipeCreateView, RecipeList, RecipeDetail, RecipeUpdate, RecetaCreateView, \
    RecetaUpdateView, RecetaFormSetView, RecetaCreateNamedView, RecetaUpdateNamedView

recipe_urls = patterns('',
    url(r'^$', RecipeDetail, name='RecipeDetail'),
    url(r'^RecipeUpdate$', RecipeUpdate.as_view(), name='RecipeUpdate'),
)

urlpatterns = patterns('',
    url(r'^$', RecipeList.as_view(), name='RecipeList'),
    url(r'^AddRecipe$', RecipeCreateView.as_view(), name='AddRecipe'),

    url(r'^RecetaCreate/$', RecetaCreateView.as_view(), name='RecetaCreate'),
    url(r'^RecetaCreateNamed/$', RecetaCreateNamedView.as_view(), name='RecetaCreateNamed'),
    url(r'^RecetaUpdate/(?P<pk>\d+)/$', RecetaUpdateView.as_view(), name='RecetaUpdate'),
    url(r'^RecetaUpdateNamed/(?P<pk>\d+)/$', RecetaUpdateNamedView.as_view(), name='RecetaUpdateNamed'),
    url(r'^(?P<pk>\d+)/$', RecetaFormSetView.as_view(), name='RecetaDetail'),

    url(r'^(?P<slug>[\w-]+).recipe/', include(recipe_urls)),

)