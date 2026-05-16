from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import LanguageRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LanguageRedirectView.as_view(), name='language_redirect'),
    path('<str:lang>/products/', include('apps.products.urls')),
    path('<str:lang>/', include('apps.core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
