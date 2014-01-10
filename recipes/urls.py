#urls.py
from django.conf.urls import patterns, url, include
from recipes.views import RecipeCreateView, RecipeList, RecipeDetail, RecipeUpdate, RecetaCreateView, RecetaUpdateView, RecetaDetailView

recipe_urls = patterns('',
    url(r'^$', RecipeDetail, name='RecipeDetail'),
    url(r'^RecipeUpdate$', RecipeUpdate.as_view(), name='RecipeUpdate'),
)

urlpatterns = patterns('',
    url(r'^$', RecipeList.as_view(), name='RecipeList'),
    url(r'^AddRecipe$', RecipeCreateView.as_view(), name='AddRecipe'),

    url(r'^RecetaCreate/$', RecetaCreateView.as_view(), name='RecetaCreate'),
    url(r'^RecetaUpdate/(?P<slug>[\w-]+)/$', RecetaUpdateView.as_view(), name='RecetaUpdate'),
    url(r'^RecetaDetail/(?P<slug>[\w-]+)/$', RecetaDetailView.as_view(), name='RecetaDetail'),

    url(r'^(?P<slug>[\w-]+).recipe/', include(recipe_urls)),

)