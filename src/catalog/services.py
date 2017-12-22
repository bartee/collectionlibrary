from django.utils.translation import ugettext as _

from .models import Collection, CollectionItem, Entity, EntityResource


def get_collections_for_user(user):
    """
    Returns all collections for a given user, appended with all public collections

    :param user:
    :return:
    """
    collections = Collection.objects.filter(owner=user).order_by('-created_at').all()
    return collections


def get_entities_for_user(user):
    """
    Returns all entities for a given user, appended with all public entities.

    @TODO add count

    :param user:
    :return:
    """
    entities = Entity.objects.filter(owner=user).order_by('name').all()
    resources = EntityResource.objects.filter(entity__in=entities).all()

    # Append the resource counters to it.
    counters = {}
    for resource in resources:
        rsrc_counter = counters.get(resource.entity.pk, {})
        if resource.entity.pk not in counters.keys():
            rsrc_counter = {}

        prev = rsrc_counter.get(resource.type, 0)
        rsrc_counter.update({resource.type: prev + 1})
        counters.update({resource.entity.pk: rsrc_counter})

    for entity in entities:
        entity.resource_counters = counters.get(entity.pk, None)

    return entities


class BaseCollectionEntityService(object):

    @staticmethod
    def get_entities(collection):
        """
        Get the entities for given collection. Raise an error by default

        :return:
        """
        raise NotImplementedError(_('BaseCollectionService has not been implemented'))


class WeeklyCollectionEntityService(BaseCollectionEntityService):

    @staticmethod
    def get_entities(collection):

        res = {}
        entities = CollectionItem.objects.filter(collection=collection).select_related().all()
        for entity in entities:
            # @TODO The entity_description is the date. Order these entities by date.
            # Takes some serious date parsing.
            res.update({entity.entry_description: entity})
        return res


collection_service_type_index = {'default': WeeklyCollectionEntityService}


def get_entities_for_collection(collection):
    """
    Return all the entities for the given collection
    :param collection:
    :return:
    """
    if isinstance(collection, Collection):
        service = collection_service_type_index.get(collection.template, None)
        if service:
            return service.get_entities(collection)

        return []
