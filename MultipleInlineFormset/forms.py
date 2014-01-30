#forms.py


from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Band, Album


class BandForm(ModelForm):
    class Meta:
        model = Band


AlbumFormSet = inlineformset_factory(Band, Album)
#CommentFormSet = inlineformset_factory(Band, Comment)