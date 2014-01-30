#models.py
from django.template.defaultfilters import slugify

__author__ = 'leovega'

from django.db import models

class Formacion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Formacion, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'forminline:formacion_detail', [str(self.slug)]

    @models.permalink
    def get_update_url(self):
        return 'forminline:formacion_update', [str(self.slug)]

    @models.permalink
    def get_delete_url(self):
        return 'forminline:formacion_delete', [str(self.slug)]


class Estudio(models.Model):
    estudio = models.ForeignKey(Formacion)
    description = models.CharField(max_length=255)