from .models import Collection, Entity, CollectionItem
from django.utils.translation import ugettext as _

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

        res = {'ma': None, 'di': None, 'wo': None, 'do': None, 'vr': None, 'za': None, 'zo': None}
        entities = CollectionItem.objects.filter(collection=collection).all()
        for entity in entities:
            res.update({entity.entry_description: entity})
        return entities


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