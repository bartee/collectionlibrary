from django import template

from catalog.entity_resource_data_handlers import ENTITY_TYPE_ICONS

register = template.Library()


@register.simple_tag
def icon_for_resourcetype(type):
    """
    Find and return the icon for a given resource type.
    Defaults to "clear", which is a cross mark in the case of MaterializeCSS's default iconset

    :param type: string
    :return: string
    """
    icon = ENTITY_TYPE_ICONS.get(type, "clear")
    return icon
