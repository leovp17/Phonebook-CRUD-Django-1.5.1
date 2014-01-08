# models.py
from django.db import models
from django.template.defaultfilters import slugify

#todo LV Aqui se construye el formulario principal, padre.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # slug = models.SlugField(blank=True)
    #
    # def __unicode__(self):
    #     return u"%s" % self.title
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super(Recipe, self).save(*args, **kwargs)
    #
    # @models.permalink
    # def get_absolute_url(self):
    #     return 'recipes:RecipeDetail', [str(self.slug)]

#todo LV Aqui se construyen los formulario secundarios, que se dependeran del padre.
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    description = models.CharField(max_length=255)


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()
