# forms.py
from django import forms
from django.forms.models import inlineformset_factory
from django.template.defaultfilters import slugify

from .models import Recipe, Ingredient, Instruction

#todo LV Este es el formulario central, tanto este como los otros dos formularios, ingredientes e instrucciones, se construyen en el model.py

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe

    #def __init__(self, *args, **kwargs):
        #super(RecipeForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(RecipeForm, self).save(commit=commit)


        if commit:
            instance.action_on_save = True
            instance.save()

        return instance

class RecipeFormAjax(forms.ModelForm):
    class Meta:
        model = Recipe

    #def __init__(self, *args, **kwargs):
        #super(RecipeForm, self).__init__(*args, **kwargs)


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction

IngredientFormSet = inlineformset_factory(Recipe, Ingredient)

InstructionFormSet = inlineformset_factory(Recipe, Instruction)