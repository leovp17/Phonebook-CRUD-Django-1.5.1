# views.py
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import IngredientFormSet, InstructionFormSet, RecipeForm
from .models import Recipe

#todo LV En este view se utiliza para desplegar el formulario, usando la forma tradicional, una pagina para el form con un success url.
class RecipeCreateView(CreateView):
    template_name = 'recipes/recipe_add.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet()
        instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

#todo LV Estos mixin se empiezan usar para trabajar con las vistas genericas, en este caso lo que capturamos son las diferentes recetas almacenadas en la base de datos
class RecipeMixin(object):
    model = Recipe

    def get_context_data(self, **kwargs):
         kwargs.update({'object_name': 'Recipe'})
         return kwargs


class RecipeList(RecipeMixin, ListView):
    template_name = 'recipes/recipe_list.html'

#todo LV Estos mixin se empiezan usar para trabajar con las vistas genericas, en este caso lo que capturamos es el detalle de la receta almacenada en la base de datos
class RecipeDetailMixin(object):
    model = Recipe

    def get_context_data(self, **kwargs):
         kwargs.update({'object_name': 'Recipe'})
         return kwargs


class RecipeDetail(RecipeDetailMixin, DetailView):
    pass

#todo LV aqui configuramos el ajax request, aqui es donde se trabaja toda la funcionalidad del formulario sin que sea persivido por el usuario.
def enterRecipe(request):

    if request.is_ajax() and request.POST:
        jres = {}
        jres['ok'] = "ok"
        form = RecipeForm(request.POST)

        #todo LV, el formulario valida primeramente al padre, si es correcto procede a usar una instancia para identificar los forms secundarios con el padre.
        if form.is_valid():
            jres['status'] = 'ok'
            recipeform = form.save(commit=False)
            ingredient_form = IngredientFormSet(request.POST, instance=recipeform)
            instruction_form = InstructionFormSet(request.POST, instance=recipeform)
            if ingredient_form.is_valid() and instruction_form.is_valid():


                form.save()
                ingredient_form.save()
                instruction_form.save()
        else:
            try:
                salida = render_to_string('recipes/recipe_list.html', locals(), RequestContext(request))
                jres['data'] = salida
                jres['status'] = 'novalido'
                return HttpResponse(json.dumps(jres))
            except Exception, e:
                salida = str(e)
                jres['status'] = 'nok'
                return HttpResponse(json.dumps(jres))

        return HttpResponse(json.dumps(jres))

    else:
        jres = {}

        jres['status'] = 'nok'
        return HttpResponse(json.dumps(jres))
