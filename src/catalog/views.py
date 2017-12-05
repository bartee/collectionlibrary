from dal import autocomplete
from django.views.generic import DetailView, FormView
from django.urls import reverse
import json
import logging
from datetime import datetime

from catalog.models import Collection, Entity, CollectionItem, Note
from catalog.services import get_entities_for_collection
from catalog.forms import CollectionEntityFormset, CollectionForm

logger = logging.getLogger(__name__)

class CollectionDetailView(DetailView):
    """
    Verify permissions as well

    """
    model = Collection
    template_name = 'organisms/collections/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        entity_list = get_entities_for_collection(context.get('object'))

        context.update({'entity_list': entity_list})
        return context


class EntitiesForUserAutocomplete(autocomplete.Select2QuerySetView):
    """
    This returns the list of entities for the given user.
    """
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        user = self.request.user
        if not user.is_authenticated:
            return Entity.objects.none()

        qs = Entity.objects.filter(owner=user).all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class CollectionCreateView(FormView):
    form_class = CollectionForm
    template_name = 'organisms/collections/create.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        return super(CollectionCreateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        The following should be used as well for the editing of the form.

        Form is valid: create a new collection with its related items
        - Aggregate the name. Shall we do that in the form? Yes.
        - Store the instance, remember the ID

        - Iterate over all related items, and create them.
        - For each related item, create a note if necessary.


        :param form:
        :return:
        """

        coll = Collection(owner=self.request.user, name=form.cleaned_data['name'], template='default')
        coll.save()

        res = json.loads(self.request.POST.get('collection_relations'))
        for item in res:
            fulldatestr = item.get('date')
            selected_entity = item.get('selection')
            notestr = item.get('note')

            shortdatestr = ' '.join(fulldatestr.split()[:4])
            shortdate = datetime.strptime(shortdatestr, "%a %b %d %Y")
            name = shortdate.strftime('%a %d %b')

            collectionitem = CollectionItem(collection=coll, entry_description=name)
            if selected_entity:
                entity_id = selected_entity.get('index')
                entity_text = selected_entity.get('display')
                if entity_id != '':
                    """
                    If no entity ID maar wel string, maak een nieuw entity ding aan.
                    """
                    try:
                        entity = Entity.objects.get(pk=entity_id)
                        collectionitem.item = entity
                    except Entity.DoesNotExist:
                        """
                        The entity with given id was not found
                        """
                        logger.warning('Entity {0} is unknown'.format(entity_id))
                elif entity_text != '':
                    entity = Entity(owner=self.request.user, name=entity_text)
                    entity.save()
                    collectionitem.item = entity

            if notestr != '':
                note = Note(author=self.request.user, value=notestr)
                note.save()

                collectionitem.notes = note

            collectionitem.save()


        return super(CollectionCreateView, self).form_valid(form)
