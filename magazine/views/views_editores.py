from magazine.models import Editor
from magazine.forms import EditorForm

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


# Create your views here.
class EditorMixin(object):
    model = Editor

    def get_success_url(self):
        return reverse('magazine:editor_list')

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Editor'})
        return kwargs


class EditorFormMixin(EditorMixin):
    form_class = EditorForm
    template_name = 'editores/editor_add.html'

    def get_success_url(self):
        return reverse('magazine:editor_list')

    def get(self, request, pk=None, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        if pk:
            self.object = Editor.objects.get(id=pk)
        else:
            self.object = None
        form_class = self.get_form_class()
        editor_form = self.get_form(form_class)

        return self.render_to_response(self.get_context_data(editor_form=editor_form))

    def post(self, request, pk=None, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        if pk:
            self.object = Editor.objects.get(id=pk)
        else:
            self.object = None

        form_class = self.get_form_class()
        editor_form = self.get_form(form_class)

        if (editor_form.is_valid()):
            return self.form_valid(editor_form)
        else:
            return self.form_invalid(editor_form)

    def form_valid(self, editor_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = editor_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, editor_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(editor_form=editor_form))


class EditorCreate(EditorFormMixin, CreateView):
    template_name = 'editores/editor_add.html'
    pass


class EditorList(EditorMixin, ListView):
    template_name = 'editores/editor_list.html'


class EditorDetail(EditorMixin, DetailView):
    template_name = "editores/editor_detail.html"
    pass


class EditorUpdate(EditorFormMixin, UpdateView):
    template_name = "editores/editor_add.html"
    pass


class EditorDelete(EditorMixin, DeleteView):
    template_name = "editores/editor_confirm_delete.html"
    pass

