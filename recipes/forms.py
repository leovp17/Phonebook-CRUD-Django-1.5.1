# forms.py
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, Instruction

#todo LV Este es el formulario central, tanto este como los otros dos formularios, ingredientes e instrucciones, se construyen en el model.py

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe

#todo LV Estos son los inlineformset, aqui se ligan los dos formularios secundarios al principal.

IngredientFormSet = inlineformset_factory(Recipe, Ingredient)

InstructionFormSet = inlineformset_factory(Recipe, Instruction)