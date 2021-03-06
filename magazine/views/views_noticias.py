from magazine.models import Noticia
from magazine.forms import NoticiaForm

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


# Create your views here.
class NoticiaMixin(object):
    model = Noticia

    def get_success_url(self):
        return reverse('magazine:noticia_list')

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Noticia'})
        return kwargs


class NoticiaFormMixin(NoticiaMixin):
    form_class = NoticiaForm
    template_name = 'noticias/noticia_add.html'

    def get_success_url(self):
        return reverse('magazine:noticia_list')

    def get(self, request, pk=None, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        if pk:
            self.object = Noticia.objects.get(id=pk)
        else:
            self.object = None
        form_class = self.get_form_class()
        noticia_form = self.get_form(form_class)

        return self.render_to_response(self.get_context_data(noticia_form=noticia_form))

    def post(self, request, pk=None, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        if pk:
            self.object = Noticia.objects.get(id=pk)
        else:
            self.object = None

        form_class = self.get_form_class()
        noticia_form = self.get_form(form_class)

        if (noticia_form.is_valid()):
            return self.form_valid(noticia_form)
        else:
            return self.form_invalid(noticia_form)

    def form_valid(self, noticia_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = noticia_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, noticia_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(noticia_form=noticia_form))


class NoticiaCreate(NoticiaFormMixin, CreateView):
    template_name = 'noticias/noticia_add.html'
    pass


class NoticiaList(NoticiaMixin, ListView):
    template_name = 'noticias/noticia_list.html'


class NoticiaDetail(NoticiaMixin, DetailView):
    template_name = "noticias/noticia_detail.html"
    pass


class NoticiaUpdate(NoticiaMixin, UpdateView):
    template_name = "noticias/noticia_add.html"
    pass


class NoticiaDelete(NoticiaMixin, DeleteView):
    template_name = "noticias/noticia_confirm_delete.html"
    pass

