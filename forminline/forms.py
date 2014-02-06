#forms.py
__author__ = 'leovega'

from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Formacion, Estudio


class FormacionForm(ModelForm):
    class Meta:
        model = Formacion


EstudioFormSet = inlineformset_factory(Formacion, Estudio)