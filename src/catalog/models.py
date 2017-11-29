import json

from django.conf import settings
from django.db import models


class PrivateShareableModel(models.Model):
    """
    A model that's got an owner, and can be shared with a list of owners.

    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    """
    A model having a creation date and maintains the latest update

    """
    created_at = models.DateTimeField(verbose_name="Creation date", auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Last update", auto_now_add=True)

    class Meta:
        abstract = True


class Collection(PrivateShareableModel, TimestampedModel):
    """
    A list of items
    """
    TYPE_LIST = (('default', 'Default Template'),)
    name = models.CharField(max_length=255)
    template = models.CharField(max_length=50, choices=TYPE_LIST)
    shared_with = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='co_owners', blank=True)

    def template_path(self):
        return "organisms"

    def __str__(self):
        return self.name

class Entity(PrivateShareableModel, TimestampedModel):
    """
    An entity that can be added into a list. It has a name, an image, an owner, it can be public as well.
    """
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Entities'


class EntityResource(models.Model):

    RESOURCE_TYPES = (('image', 'Image'), ('url','Link'))

    entity = models.ForeignKey(to=Entity, on_delete=models.CASCADE, blank=True, default=None)

    type = models.CharField(max_length=25, choices=RESOURCE_TYPES, default='url')
    data = models.TextField()
    description = models.TextField()

    def __str__(self):
        return "{0} - ({1})".format(self.entity, self.type)

    @property
    def data_dict(self):
        return json.loads(self.data)

class Note(models.Model):
    """
    A simple model to add multiple notes to an item in a list.

    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        if len(self.value) > 5 :
            return "{}...".format(self.value[:4])
        return self.value


class CollectionItem(models.Model):
    """
    Relational model for managing items on a list.

    list
    entity
    entry_description
    note ~

    """
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    item = models.ForeignKey(Entity, on_delete=models.CASCADE)
    entry_description = models.CharField(max_length=100)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE)
