from django.views.generic.list import ListView
from micrud.models import Category, Person
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from micrud.forms import CategoryForm, PersonForm
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

class CategoryMixin(object):
    model = Category
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Category'})
        return kwargs

class CategoryFormMixin(CategoryMixin):
    form_class = CategoryForm
    template_name = 'micrud/object_form.html'

class CategoryList(CategoryMixin, ListView):
    template_name = 'micrud/object_list.html'

class CategoryDetail(CategoryMixin, DetailView):
    pass

class NewCategory(CategoryFormMixin, CreateView):
    pass

class EditCategory(CategoryFormMixin, UpdateView):
    pass

class DeleteCategory(CategoryMixin, DeleteView):
    template_name = 'micrud/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('micrud:category_list')

class PersonMixin(object):
    model = Person
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Person'})
        return kwargs

class PersonFormMixin(PersonMixin):
    form_class = PersonForm
    template_name = 'micrud/object_form.html'

class PeopleList(PersonMixin, ListView):
    template_name = 'micrud/object_list.html'

class ViewPerson(PersonMixin, DetailView):
    pass

class NewPerson(PersonFormMixin, CreateView):
    pass

class EditPerson(PersonFormMixin, UpdateView):
    pass

class KillPerson(PersonMixin, DeleteView):
    template_name = 'micrud/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('micrud:people_list')

class ViewCategory(PersonMixin, ListView):
    template_name = 'micrud/object_list.html'
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return super(ViewCategory, self).get_queryset().filter(category=self.category)