#views.py
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import BandForm, AlbumFormSet, CommentFormSet, GenreForm
from .models import Band, Genre



class GenreMixin(object):
    model = Genre


class GenreFormMixin(GenreMixin):
    form_class = GenreForm

    def get_success_url(self):
        return reverse('mif:genre_list')

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            self.object = Genre.objects.get(id=pk)
        else:
            self.object = None

        form_class = self.get_form_class()
        genre_form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(
                genre_form=genre_form
            )
        )

    def post(self, request, pk=None, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        if pk:
            self.object = Genre.objects.get(id=pk)
        else:
            self.object = None

        form_class = self.get_form_class()
        genre_form = self.get_form(form_class)

        if (genre_form.is_valid()):
            return self.form_valid(genre_form)
        else:
            return self.form_invalid(genre_form)

    def form_valid(self, genre_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = genre_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, genre_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(genre_form=genre_form)
        )


class GenreCreate(GenreFormMixin, CreateView):
    pass
    template_name = "genres/genre_add.html"

class GenreList(GenreMixin,ListView):
    template_name = "genres/genre_list.html"
    pass


class BandMixin(object):
    model = Band

    def get_success_url(self):
        return reverse('mif:band_list')

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Band'})
        return kwargs


class BandFormMixin(BandMixin):
    form_class = BandForm
    template_name = 'bands/band_add.html'

    def get_success_url(self):
        return reverse('mif:band_list')

    def get(self, request, pk=None, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        if pk:
            self.object = Band.objects.get(id=pk)
        else:
            self.object = None
        form_class = self.get_form_class()
        band_form = self.get_form(form_class)

        #info POM forms inline buscan modelos asociados a la instancia padre
        album_form = AlbumFormSet(instance=self.object)

        comment_form = CommentFormSet(instance=self.object)

        return self.render_to_response(
            self.get_context_data(band_form=band_form,
                                  album_form=album_form,
                                  comment_form=comment_form, ))

    def post(self, request, pk=None, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        if pk:
            self.object = Band.objects.get(id=pk)
        else:
            self.object = None

        form_class = self.get_form_class()
        band_form = self.get_form(form_class)

        album_form = AlbumFormSet(self.request.POST, instance=self.object)

        comment_form = CommentFormSet(self.request.POST, instance=self.object)

        if (band_form.is_valid() and album_form.is_valid() and comment_form.is_valid()):
            return self.form_valid(band_form, album_form, comment_form)
        else:
            return self.form_invalid(band_form, album_form, comment_form)

    def form_valid(self, band_form, album_form, comment_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = band_form.save()
        album_form.instance = self.object
        album_form.save()
        comment_form.instance = self.object
        comment_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, band_form, album_form, comment_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(band_form=band_form,
                                  album_form=album_form,
                                  comment_form=comment_form))


class BandCreate(BandFormMixin, CreateView):
    template_name = 'bands/band_add.html'
    pass


class BandList(BandMixin, ListView):
    template_name = 'bands/band_list.html'


class BandDetail(BandMixin, DetailView):
    template_name = "bands/band_detail.html"
    pass


class BandUpdate(BandFormMixin, UpdateView):
    #template_name = "bands/band_add.html"
    pass


class BandDelete(BandMixin, DeleteView):
    template_name = "bands/band_confirm_delete.html"
    pass