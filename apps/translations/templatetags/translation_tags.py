from django import template
from apps.translations.utils import get_translated_field

register = template.Library()


@register.simple_tag
def trans_field(obj, field_name):
    return get_translated_field(obj, field_name)
