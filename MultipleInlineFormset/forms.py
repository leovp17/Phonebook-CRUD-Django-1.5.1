#forms.py


from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Band, Album, Comment, Track, Genre


class BandForm(ModelForm):
    class Meta:
        model = Band

class GenreForm(ModelForm):
    class Meta:
        model = Genre

    def is_valid(self):
        valid = super(GenreForm, self).is_valid()
        if not valid:
            return valid

        try:
            genre = Genre.objects.get(name = self.cleaned_data["name"])
            return False
        except Genre.DoesNotExist:
            return True


AlbumFormSet = inlineformset_factory(Band, Album)
CommentFormSet = inlineformset_factory(Band, Comment)

#TODO: [POM] InlineFormSet anidados de mas de dos niveles no es soportado por la libreria, jquery.formset.js. Modificar libreria para soportar InlineFormSet anidados de mas de dos niveles
#TrackFormSet = inlineformset_factory(Album, Track)