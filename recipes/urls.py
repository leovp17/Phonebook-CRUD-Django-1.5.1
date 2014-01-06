#urls.py
from django.conf.urls import patterns, url
from recipes.views import RecipeCreateView, RecipeList, show_edu

urlpatterns = patterns('',
    url(r'^$', RecipeList.as_view(), name='RecipeList'),
    url(r'^AddRecipe$', RecipeCreateView.as_view(), name='AddRecipe'),

)