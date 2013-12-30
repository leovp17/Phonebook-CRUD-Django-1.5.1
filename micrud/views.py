from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.forms.formsets import BaseFormSet, formset_factory
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.generic.list import ListView
from micrud.models import Category, Person
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from micrud.forms import CategoryForm, PersonForm, PersonFormAjax
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import BookForm

import json

from django.http import HttpResponse


class CategoryMixin(object):
    model = Category

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Category'})
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
        kwargs.update({'object_name': 'Person'})
        return kwargs


class PersonFormMixin(PersonMixin):
    form_class = PersonForm
    template_name = 'micrud/object_form.html'


class PersonFormAjaxMixin(PersonMixin):
    form_class = PersonFormAjax
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


class AjaxableResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class NewPersonAjax(AjaxableResponseMixin, PersonFormAjaxMixin, CreateView):
    pass


def enter(request):
    if request.is_ajax() and request.POST:
        jres = {}
        jres['ok'] = "ok"

        form = PersonFormAjax(request.POST)
        if form.is_valid():
            jres['status'] = 'ok'
            form.save()
        else:
            try:
                salida = render_to_string('micrud/object_form.html', locals(), RequestContext(request))
                jres['data'] = salida
                jres['status'] = 'novalido'
                return HttpResponse(json.dumps(jres))
            except Exception,e:
                salida=str(e)
                jres['status'] = 'nok'
                return HttpResponse(json.dumps(jres))

        return HttpResponse(json.dumps(jres))

    else:
        jres = {}

        jres['status'] = 'nok'
        return HttpResponse(json.dumps(jres))




#adding multiple forms with formset
def create_multiple_books(request, publisher_id):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    BookFormset = formset_factory(BookForm, max_num=10, formset=RequiredFormSet)
    if request.method == 'POST':
        book_formset = BookFormset(request.POST, request.FILES)
        if book_formset.is_valid():
            for form in book_formset.forms:
                obj = form.save(commit=False)
                obj.publisher_id = publisher_id
                obj.save()
            return redirect(reverse('created'))
    else:
        book_formset = BookFormset()
    c = {'book_formset': book_formset,
         'publisher_id':publisher_id,
        }
    c.update(csrf(request))
    return render_to_response('micrud/template.html', c, context_instance=RequestContext(request))

