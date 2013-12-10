from django import forms
from micrud.models import Category, Person

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
<<<<<<< HEAD
        fields = ('first_name', 'last_name', 'category', 'proximity', 'home_phone', 'cell_phone', 'email',)

class PersonFormAjax(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'category', 'proximity',)
=======
        fields = ('first_name', 'last_name', 'category', 'proximity', 'home_phone', 'cell_phone', 'email',)
>>>>>>> Phonebook-CRUD-Django-1.5.1/master
