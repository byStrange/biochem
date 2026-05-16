from apps.products.models import Category


def global_context(request):
    return {
        'brand_name': 'Biochem',
        'nav_categories': Category.objects.filter(is_active=True).order_by('order'),
        'current_language': getattr(request, 'LANGUAGE_CODE', 'en'),
        'available_languages': [
            ('en', 'English'),
            ('ru', 'Russian'),
            ('uz', 'Uzbek'),
        ],
    }
