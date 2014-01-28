#forms.py

from django import forms
from django.forms.models import inlineformset_factory
from inlines.models import Candidato, Formacion

CandidatoEstudioFormSet = inlineformset_factory(Candidato, Formacion, extra=1, max_num=10, can_delete=True, fields=('field_of_study', 'start_date', 'end_date', 'school_name'))
