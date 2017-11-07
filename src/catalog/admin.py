from django.contrib import admin

from .models import Entity, Collection, CollectionItem, EntityResource, Note

# Register your models here.

@admin.register(Entity)
class EntityModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_public', 'created_at', 'updated_at')
    exclude = ("created_at", "updated_at", "is_public", "owner")

@admin.register(EntityResource)
class EntityResourceModelAdmin(admin.ModelAdmin):
    list_display = ('entity', 'type', 'data', 'description')

@admin.register(Collection)
class CollectionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'template', 'owner', 'is_public', 'created_at', 'updated_at')
    exclude = ("created_at", "updated_at", "is_public", "owner")


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

