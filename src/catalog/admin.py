from django.contrib import admin
from django.utils.html import format_html
import json
from catalog.forms import EntityResourceForm, CollectionForm
from catalog.models import (Collection, CollectionItem, Entity, EntityResource,
                            Note)

from catalog.data_handlers import ENTITY_TYPE_HANDLERS, LinkEntityResourceTypeHandler, ImageEntityResourceTypeHandler, \
    BaseEntityResourceTypeHandler


class CollectionItemInline(admin.TabularInline):
    model = CollectionItem


@admin.register(Entity)
class EntityModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_public', 'created_at', 'updated_at')
    exclude = ("created_at", "updated_at", "is_public", "owner")

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()


@admin.register(EntityResource)
class EntityResourceModelAdmin(admin.ModelAdmin):
    form = EntityResourceForm

    list_display = ('entity', 'type', 'resource_content')
    radio_fields = {'type': admin.HORIZONTAL}

    def resource_content(self, form):
        type = form.type
        handler_class = ENTITY_TYPE_HANDLERS.get(type,BaseEntityResourceTypeHandler)
        handler_instance = handler_class()
        return format_html(handler_instance.display_content(form,'compact'))

    def get_form(self, request, obj=None, **kwargs):
        form = super(EntityResourceModelAdmin, self).get_form(request, obj, **kwargs)
        if obj:

            handler_class = ENTITY_TYPE_HANDLERS.get(obj.type, BaseEntityResourceTypeHandler)
            handler_instance = handler_class()

            initial_dataset = handler_instance.parse_data(obj.data)
            for key,value in initial_dataset.items():
                form.base_fields[key].initial = value
        return form

    def save_model(self, request, obj, form, change):
        type = obj.type
        # Transform the form input to valid instance data.
        handler_class = ENTITY_TYPE_HANDLERS.get(type, BaseEntityResourceTypeHandler)
        handler_instance = handler_class()
        obj.data = json.dumps(handler_instance.get_data(form.cleaned_data))
        obj.save()


@admin.register(Collection)
class CollectionModelAdmin(admin.ModelAdmin):
    form = CollectionForm
    list_display = ('name', 'template', 'owner', 'is_public', 'created_at', 'updated_at')
    exclude = ("created_at", "updated_at", "is_public", "owner", "shared_with", "template")

    inlines = [
        CollectionItemInline
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.template = "default"
        obj.save()


@admin.register(CollectionItem)
class CollectionItemModelAdmin(admin.ModelAdmin):
    list_display = ('collection', 'item', 'entry_description')


@admin.register(Note)
class NoteModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'value')
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
