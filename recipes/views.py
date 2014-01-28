# views.py
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, \
    NamedFormsetsMixin

from .forms import RecipeForm, IngredientForm, InstructionForm, RecipeFormAjax, IngredientFormSet, InstructionFormSet
from .models import Recipe, Ingredient, Instruction


"""
    Django-extra-views
    DOCS: http://django-extra-views.readthedocs.org/en/latest/views.html
"""

class IngredientInline(InlineFormSet):
    model = Ingredient
    """
        Por default el inlineFormSet agrega dos campos[extra] del formulario.
    """
    extra = 1
    max_num = None
    can_delete = True


class InstructionInline(InlineFormSet):
    model = Instruction
    extra = 1
    max_num = None
    can_delete = True


class RecetaCreateView(CreateWithInlinesView):
    model = Recipe
    inlines = [IngredientInline, InstructionInline]
    template_name = 'recipes/receta_add.html'

    def get_success_url(self):
        return '../RecetaDetail/%i' % self.object.slug


class RecetaCreateViewAjax(CreateWithInlinesView):
    model = Recipe
    inlines = [IngredientInline, InstructionInline]
    template_name = 'recipes/receta_add.html'


class RecetaUpdateView(UpdateWithInlinesView):
    model = Recipe
    form_class = RecipeForm
    inlines = [IngredientInline, InstructionInline]
    template_name = 'recipes/receta_add.html'

    def get_success_url(self):
        return '../../%i' % self.object.slug


class RecetaUpdateNamedView(NamedFormsetsMixin, RecetaUpdateView):
    inlines_names = ['ingredientes','instrucciones']
    template_name = 'recipes/receta_add_namedFormsets.html'

    """def get_success_url(self):
        return '../../RecetaDetail/%i' % self.object.slug"""


class RecetaMixin(object):
    model = Recipe
    inlines = [IngredientInline, InstructionInline]

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Recetas'})
        return kwargs


class RecetaList(RecetaMixin, ListView):
    template_name = 'recipes/recipe_list.html'


def RecetaDetail(request, slug):

    recetas = Recipe.objects.get(slug=slug)
    id = recetas.id

    ingredientes = Ingredient.objects.filter(recipe_id__exact=id)
    instruction = Instruction.objects.filter(recipe_id__exact=id)

    return render_to_response('recipes/recipe_detail.html', locals(), RequestContext(request))



class RecetaCreateNamedView(NamedFormsetsMixin, RecetaCreateView):
    inlines_names = ['ingredientes','instrucciones']
    template_name = 'recipes/receta_add_namedFormsets.html'


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
                jres['status'] = 'novalido'
                salida = render_to_string('recipes/receta_add_namedFormsets.html', locals(), RequestContext(request))
                jres['data'] = salida
                print("algo no esta validado")
        else:
            try:

                ingredient_form = IngredientFormSet(request.POST)
                instruction_form = InstructionFormSet(request.POST)
                salida = render_to_string('recipes/receta_add_namedFormsets.html', locals(), RequestContext(request))
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
