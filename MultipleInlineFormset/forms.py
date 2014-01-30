#forms.py


from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Band, Album, Comment, Track


class BandForm(ModelForm):
    class Meta:
        model = Band


AlbumFormSet = inlineformset_factory(Band, Album)
CommentFormSet = inlineformset_factory(Band, Comment)

#TODO: [POM] InlineFormSet anidados de mas de dos niveles no es soportado por la libreria, jquery.formset.js. Modificar libreria para soportar InlineFormSet anidados de mas de dos niveles
#TrackFormSet = inlineformset_factory(Album, Track)