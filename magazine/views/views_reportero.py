from magazine.models import Reportero
from magazine.forms import ReporteroForm

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


# Create your views here.
class ReporteroMixin(object):
    model = Reportero

    def get_success_url(self):
        return reverse('magazine:reportero_list')

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Reportero'})
        return kwargs


class ReporteroFormMixin(ReporteroMixin):
    form_class = ReporteroForm
    template_name = 'reporteros/reportero_add.html'

    def get_success_url(self):
        return reverse('magazine:reportero_list')

    def get(self, request, pk=None, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        if pk:
            self.object = Reportero.objects.get(id=pk)
        else:
            self.object = None
        form_class = self.get_form_class()
        reportero_form = self.get_form(form_class)

        return self.render_to_response(self.get_context_data(reportero_form=reportero_form))

    def post(self, request, pk=None, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        if pk:
            self.object = Reporter.objects.get(id=pk)
        else:
            self.object = None

        form_class = self.get_form_class()
        reportero_form = self.get_form(form_class)

        if (reportero_form.is_valid()):
            return self.form_valid(reportero_form)
        else:
            return self.form_invalid(reportero_form)

    def form_valid(self, reportero_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = reportero_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, reportero_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(reportero_form=reportero_form))


class ReporteroCreate(ReporteroFormMixin, CreateView):
    template_name = 'reporteros/reportero_add.html'
    pass


class ReporteroList(ReporteroMixin, ListView):
    template_name = 'reporteros/reportero_list.html'


class ReporteroDetail(ReporteroMixin, DetailView):
    template_name = "reporteros/reportero_detail.html"
    pass


class ReporteroUpdate(ReporteroFormMixin, UpdateView):
    template_name = "reporteros/reportero_add.html"
    pass


class ReporteroDelete(ReporteroMixin, DeleteView):
    template_name = "reporteros/reportero_confirm_delete.html"
    pass

