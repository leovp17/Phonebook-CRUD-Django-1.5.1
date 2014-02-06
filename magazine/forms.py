from django.forms import ModelForm

from .models import Noticia, Reportero, Editor, Director


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia


class ReporteroForm(ModelForm):
    class Meta:
        model = Reportero
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'magazine']


class EditorForm(ModelForm):
    class Meta:
        model = Editor
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'magazine']


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'magazine']