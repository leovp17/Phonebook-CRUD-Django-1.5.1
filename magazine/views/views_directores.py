from magazine.models import Director
from magazine.forms import DirectorForm

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


# Create your views here.
class DirectorMixin(object):
    model = Director

    def get_success_url(self):
        return reverse('magazine:director_list')

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Director'})
        return kwargs


class DirectorFormMixin(DirectorMixin):
    form_class = DirectorForm
    template_name = 'directores/director_add.html'

    def get_success_url(self):
        return reverse('magazine:director_list')

    def get(self, request, pk=None, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        if pk:
            self.object = Director.objects.get(id=pk)
        else:
            self.object = None
        form_class = self.get_form_class()
        director_form = self.get_form(form_class)

        return self.render_to_response(self.get_context_data(director_form=director_form))

    def post(self, request, pk=None, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        if pk:
            self.object = Director.objects.get(id=pk)
        else:
            self.object = None

        form_class = self.get_form_class()
        director_form = self.get_form(form_class)

        if (director_form.is_valid()):
            return self.form_valid(director_form)
        else:
            return self.form_invalid(director_form)

    def form_valid(self, director_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = director_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, director_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(director_form=director_form))


class DirectorCreate(DirectorFormMixin, CreateView):
    template_name = 'directores/director_add.html'
    pass


class DirectorList(DirectorMixin, ListView):
    template_name = 'directores/director_list.html'


class DirectorDetail(DirectorMixin, DetailView):
    template_name = "directores/director_detail.html"
    pass


class DirectorUpdate(DirectorFormMixin, UpdateView):
    template_name = "directores/director_add.html"
    pass


class DirectorDelete(DirectorMixin, DeleteView):
    template_name = "directores/director_confirm_delete.html"
    pass

