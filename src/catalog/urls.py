from django.urls import path

from .views import CollectionDetailView

urlpatterns = [
    path('collection/<int:pk>/', CollectionDetailView.as_view(), name="collection_detail"),
]