from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Genre(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200)


class Band(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre)

    @models.permalink
    def get_absolute_url(self):
        #info POM Para utilizar el reverse cuando hay mas de una aplicacion, colocar el nombre de la aplicacion
        return 'mif:band_detail', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'mif:band_update', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'mif:band_delete', [self.id]


class Comment(models.Model):
    def __unicode__(self):
        return slugify(self.comment)

    username = models.CharField(max_length=200, default=None, null=True)
    comment = models.CharField(max_length=500)
    band = models.ForeignKey(Band)


class Album(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200)
    band = models.ForeignKey(Band)


class Track(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album)
