from django.utils import translation


def get_translated_field(obj, field_name, lang=None):
    if lang is None:
        lang = translation.get_language()
    if lang == 'en':
        return getattr(obj, field_name, '') or ''
    translated = getattr(obj, f'{field_name}_{lang}', '') or ''
    if translated:
        return translated
    return getattr(obj, field_name, '') or ''
