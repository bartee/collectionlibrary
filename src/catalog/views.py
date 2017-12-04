from dal import autocomplete
from django.views.generic import DetailView, FormView
from django.urls import reverse

from catalog.models import Collection, Entity
from catalog.services import get_entities_for_collection
from catalog.forms import CollectionEntityFormset, CollectionForm


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

        return super(CollectionCreateView, self).form_valid(form)
