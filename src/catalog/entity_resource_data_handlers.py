from django.utils.translation import ugettext as _
from django import forms
from cloudinary import CloudinaryImage
import json


class BaseEntityResourceTypeHandler(object):

    def validate(self, data):
        """
        Return false by default

        :param data:
        :return:
        """
        return False

    def parse_data(self, data, *args, **kwargs):
        """

        :param data:
        :param args:
        :param kwargs:
        :return: a per-key dictionary of initial values
        """
        raise NotImplementedError(_('This Entity Resource type is not implemented'))

    def get_data(self, cleaned_data, *args, **kwargs):
        raise NotImplementedError(_('This Entity Resource type is not implemented'))

    def display_content(self, instance, style='full', *args, **kwargs):
        return False


class LinkEntityResourceTypeHandler(BaseEntityResourceTypeHandler):

    def validate(self, data):
        """
        Required field: url

        :param data:
        :return:
        """
        url = data.get('url')
        if not url:
            raise forms.ValidationError(_('No URL was entered while the type was set to link.'))

    def parse_data(self, data, *args, **kwargs):
        result = json.loads(data)
        return {'url': result.get('src')}

    def get_data(self, cleaned_data, *args, **kwargs):
        url = cleaned_data.get('url')
        return {'src': url}

    def display_content(self, instance, style='full', *args, **kwargs):
        data_dict = json.loads(instance.data)
        url = data_dict.get('src')
        return '<a href="{url}" target="_blank">{text}</a>'.format(url=url, text=instance.description)


class ImageEntityResourceTypeHandler(BaseEntityResourceTypeHandler):
    """
    Image, using Cloudinary for data store.

    """
    def validate(self, data):
        image = data.get('image')
        if not image:
            raise forms.ValidationError(_('No Image was entered while the type was set to image.'))

    def parse_data(self, data, *args, **kwargs):
        data = kwargs.get('data')
        result = json.loads(data)
        return result.get('image')

    def get_data(self, cleaned_data, *args, **kwargs):
        image_obj = cleaned_data.get('image')
        return {'image_id': image_obj.public_id, 'metadata': image_obj.metadata}

    def display_content(self, instance, style='full', *args, **kwargs):
        data_dict = json.loads(instance.data)
        image_id = data_dict.get('image_id')
        img = CloudinaryImage(public_id=image_id)
        if style == 'full':
            return img.image()
        return img.image(height=50)


class TextEntityResourceTypeHandler(BaseEntityResourceTypeHandler):
    """
    Plain text field, to attach to entities
    """
    def validate(self, data):
        text = data.get('text')
        if not text:
            raise forms.ValidationError(_('No text was entered, while the type was set to text'))

    def parse_data(self, data, *args, **kwargs):
        result = json.loads(data)
        return result.get('text')

    def get_data(self, cleaned_data, *args, **kwargs):
        text = cleaned_data.get('text')
        return {'text': text}

    def display_content(self, instance, style='full', *args, **kwargs):
        data_dict = json.loads(instance.data)
        return data_dict.get('text')


ENTITY_TYPE_HANDLERS = {
    'url': LinkEntityResourceTypeHandler,
    'image': ImageEntityResourceTypeHandler,
    'text': TextEntityResourceTypeHandler
}

ENTITY_TYPE_ICONS = {
    'url': 'link',
    'image': 'image',
    'text': 'short_text'
}