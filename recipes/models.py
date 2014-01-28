# models.py
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


#todo LV Aqui se construye el formulario principal, padre.
class Recipe(models.Model):
    title = models.CharField('Nombre de la receta', max_length=255)
    description = models.TextField('Descripcion de la receta')
    slug = models.SlugField(blank=True)
    action_on_save = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Recipe, self).save(*args, **kwargs)
"""
    def __unicode__(self):
        return u"%s" % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'recipes:RecetaDetail', [str(self.slug)]

    @models.permalink
    def get_update_url(self):
        return 'recipes:RecetaUpdateNamed', [str(self.slug)]

    @models.permalink
    def get_success_url(self):
        return 'recipes', [str(self)]lf)]
"""

#todo LV Aqui se construyen los formulario secundarios, que se dependeran del padre.
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    description = models.CharField('Ingrediente', max_length=255)


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    number = models.PositiveSmallIntegerField('Paso')
    description = models.TextField('Descripcion')
