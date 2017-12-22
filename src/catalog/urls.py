from django.urls import path

from .views import (CollectionCreateView, CollectionDetailView,
                    EntitiesForUserAutocomplete)

urlpatterns = [
    path('collection/<int:pk>/', CollectionDetailView.as_view(), name="collection_detail"),
    path('collection/create/', CollectionCreateView.as_view(), name="collection_create"),
    path('entity_autocomplete/', EntitiesForUserAutocomplete.as_view(), name="entity_user_autocomplete"),
]
