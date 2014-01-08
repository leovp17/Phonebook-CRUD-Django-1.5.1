#urls.py
from django.conf.urls import patterns, url, include
from recipes.views import RecipeCreateView, RecipeList, RecipeDetail

recipe_urls = patterns('',
    url(r'^$', RecipeDetail.as_view(), name='RecipeDetail'),
)

urlpatterns = patterns('',
    url(r'^$', RecipeList.as_view(), name='RecipeList'),
    url(r'^AddRecipe$', RecipeCreateView.as_view(), name='AddRecipe'),

    url(r'^(?P<slug>[\w-]+).recipe/', include(recipe_urls)),

)