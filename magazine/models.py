from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Revista(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=200)


class Reportero(User):
    def __unicode__(self):
        return self.name

    magazine = models.ForeignKey(Revista)


class Editor(User):
    def __unicode__(self):
        return self.name

    magazine = models.ForeignKey(Revista)


class Director(User):
    def __unicode__(self):
        return self.name

    magazine = models.ForeignKey(Revista)


class Noticia(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=200)
    noticia = models.TextField()
    publication_date = models.DateField(auto_created=True)
    edited_date = models.DateField(auto_now=True)
    magazine = models.ForeignKey(Revista)
