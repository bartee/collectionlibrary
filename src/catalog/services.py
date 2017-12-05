from django.utils.translation import ugettext as _

from .models import Collection, CollectionItem, Entity


def get_collections_for_user(user):
    """
    Returns all collections for a given user, appended with all public collections

    :param user:
    :return:
    """
    collections = Collection.objects.filter(owner=user).all()
    return collections


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
