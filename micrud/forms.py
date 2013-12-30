from django import forms
from micrud.models import Category, Person, Publisher, Book

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'category', 'proximity', 'home_phone', 'cell_phone', 'email',)

class PersonFormAjax(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'category', 'proximity',)



#adding multiple forms with formset
class PublisherForm(forms.ModelForm):
    model = Publisher

class BookForm(forms.ModelForm):
    model = Book
    exclude = ('generic', 'publisher_id',)

    def __init__(self, *args, **kwargs):

        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'id':'inputId', 'class':'input-block-level', 'placeholder':'Name'}
        self.fields['name'].error_messages = {'required': 'Please enter name'}

        self.fields['age'].widget.attrs = {'id':'inputId', 'class':'input-block-level', 'placeholder':'Age'}
        self.fields['age'].error_messages = {'required': 'Please enter age'}