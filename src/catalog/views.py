from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from catalog.services import get_entities_for_collection
from catalog.models import Collection

class CollectionDetailView(DetailView):
    """
    Verify permissions as well

    """
    model = Collection
    template_name = 'organisms/collections/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        entities = get_entities_for_collection(context.get('object'))

        context.update({'entities': entities})
        return context


