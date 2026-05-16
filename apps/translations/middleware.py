from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect
from django.urls import resolve, Resolver404


class LocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = self._get_language_from_path(request.path_info)
        if lang and lang in dict(settings.LANGUAGES):
            translation.activate(lang)
            request.LANGUAGE_CODE = lang
        else:
            request.LANGUAGE_CODE = settings.LANGUAGE_CODE
        response = self.get_response(request)
        return response

    def _get_language_from_path(self, path):
        parts = path.strip('/').split('/')
        if parts:
            return parts[0]
        return None
