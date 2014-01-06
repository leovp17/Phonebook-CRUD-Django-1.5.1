from django.db import models
from django.contrib.contenttypes import generic
from django.template.defaultfilters import slugify
from django.contrib.localflavor.us.models import PhoneNumberField


class Category(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return u"%s" % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'micrud:category_detail', [str(self.slug)]

    @models.permalink
    def get_update_url(self):
        return 'micrud:category_update', [str(self.slug)]

    @models.permalink
    def get_delete_url(self):
        return 'micrud:category_delete', [str(self.slug)]


class Person(models.Model):
    PROXIMITY_LIST = (
        (0, 'Not sure'),
        ('Friends', (
            (10, 'Best friends forever'),
            (20, 'Close friends'),
            (30, 'Distant friends'),
            (40, 'Enemies til the end')
        )),
        ('Family', (
            (50, 'Super close'),
            (60, 'Only on occasion'),
            (70, 'Only at funerals'),
            (80, 'Family grouch!')
        )),
    )
    first_name = models.CharField(max_length=60, help_text='Their first name')
    last_name = models.CharField(max_length=80, blank=True, help_text='Do you know it?')
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, help_text='File this person where?')
    proximity = models.PositiveSmallIntegerField(choices=PROXIMITY_LIST, help_text='How much of a distance to keep?')
    home_phone = PhoneNumberField(blank=True)
    cell_phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True, help_text='Do they have an Email address?')
    added_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'people'
        ordering = ['last_name']

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name) if self.last_name != '' else u"%s" % self.first_name

    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name) if self.last_name != '' else u"%s" % self.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        return super(Person, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'micrud:person_detail', [str(self.slug)]

    @models.permalink
    def get_update_url(self):
        return 'micrud:person_update', [str(self.slug)]

    @models.permalink
    def get_delete_url(self):
        return 'micrud:person_delete', [str(self.slug)]