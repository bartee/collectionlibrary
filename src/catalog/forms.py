from dal import autocomplete
from django import forms
from django.forms.models import inlineformset_factory

from catalog.models import Collection, EntityResource, CollectionItem

from catalog.data_handlers import ENTITY_TYPE_HANDLERS, BaseEntityResourceTypeHandler, \
    LinkEntityResourceTypeHandler, ImageEntityResourceTypeHandler

from django.contrib.admin.widgets import AdminDateWidget

class EntityResourceForm(forms.ModelForm):

    url = forms.URLField(required=False);
    image = forms.ImageField(required=False);

    class Meta:
        model = EntityResource
        exclude = ('data',)
        fields = ('__all__')
        widgets = {
            'entity': autocomplete.ModelSelect2(url='entity_user_autocomplete')
        }

    def clean(self):
        """
        Clean the data
        :return:
        """
        cleaned_data = super(EntityResourceForm, self).clean()
        type = cleaned_data.get('type')

        if type not in [index[0] for index in EntityResource.RESOURCE_TYPES]:
            raise forms.ValidationError(_('{type} is an unknown EntityResource type'.format(type=type)))

        handler = ENTITY_TYPE_HANDLERS.get(type, BaseEntityResourceTypeHandler)

        instance = handler()
        instance.validate(cleaned_data)


class CollectionForm(forms.ModelForm):

    start_date = forms.DateField(widget=AdminDateWidget(attrs={'class':'datepicker'}))
    end_date = forms.DateField(widget=AdminDateWidget(attrs={'class':'datepicker'}))
    name = forms.CharField()

    class Meta:
        model = Collection
        exclude = ('template', 'shared_with', 'name')
        fields = ()

    class Media:
        js = ('js/class.js', 'js/catalog/collection_form_handlers.js',)


    def clean(self):
        """
        Create the name from the start date, the end date and the

        :return:
        """
        cleaned_data = super(CollectionForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        verbose_name = cleaned_data.get('verbose_name')


class CollectionEntityForm(forms.ModelForm):
    """
    CollectionEntityForm
    """

    def __init__(self, *args, **kwargs):
        super(CollectionEntityForm, self).__init(*args,**kwargs)

    class Meta:
        model = CollectionItem
        fields = ('__all__')


CollectionEntityFormset = inlineformset_factory(Collection, CollectionItem, form=CollectionEntityForm,
                                                can_delete=True, extra=3)