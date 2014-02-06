#views.py
__author__ = 'leovega'

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from .forms import EstudioFormSet, FormacionForm
from .models import Formacion


class FormacionCreateView(CreateView):
    template_name = 'forminline/formacion_add.html'
    model = Formacion
    form_class = FormacionForm
    success_url = '/forminline/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        estudio_form = EstudioFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  estudio_form=estudio_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        estudio_form = EstudioFormSet(self.request.POST)
        if (form.is_valid() and estudio_form.is_valid()):
            return self.form_valid(form, estudio_form)
        else:
            return self.form_invalid(form, estudio_form)

    def form_valid(self, form, estudio_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        estudio_form.instance = self.object
        estudio_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, estudio_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  estudio_form=estudio_form))


class FormacionMixin(object):
    model = Formacion

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Formacion'})
        return kwargs


class FormacionFormMixin(FormacionMixin):
    form_class = FormacionForm
    template_name = 'forminline/formacion_add.html'


class FormacionList(FormacionMixin, ListView):
    template_name = 'forminline/formacion_list.html'


class NewFormacion(FormacionFormMixin, CreateView):
    pass

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        estudio_form = EstudioFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  estudio_form=estudio_form))


class EditFormacion(FormacionFormMixin, UpdateView):
    pass


class ViewFormacion(FormacionMixin, DetailView):
    pass