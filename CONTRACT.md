# Biochem Corporate Website — Architecture Contract

This document defines the contracts between all subsystems. All agents must adhere to these interfaces.

---

## 1. Directory Structure (All Agents)

```
biochem_project/
├── config/                  # Agent 1: settings, urls, wsgi, asgi
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── core/                # Agent 3 + 4: homepage, about, contact, story, sustainability
│   │   ├── __init__.py
│   │   ├── models.py        # PageContent, ContactMessage
│   │   ├── admin.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   ├── products/            # Agent 1 + 3: products, categories
│   │   ├── __init__.py
│   │   ├── models.py        # Product, Category
│   │   ├── admin.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── cms/                 # Agent 1: reusable content blocks
│   │   ├── __init__.py
│   │   ├── models.py        # ContentBlock, HeroSlide
│   │   └── admin.py
│   └── translations/        # Agent 4: utilities, middleware
│       ├── __init__.py
│       ├── utils.py         # get_translated_field
│       ├── middleware.py    # LocaleMiddleware
│       └── template_tags.py # {% trans_field obj "name" %}
├── templates/
│   ├── base.html            # Agent 3
│   ├── includes/            # Agent 3 + 4
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── language_switcher.html
│   │   └── head_meta.html
│   └── biochem/
│       ├── home.html
│       ├── product_list.html
│       ├── product_detail.html
│       ├── story.html
│       ├── sustainability.html
│       └── contact.html
├── static/
│   ├── css/
│   │   ├── variables.css    # Agent 2
│   │   ├── components.css   # Agent 2
│   │   └── main.css         # Agent 2
│   ├── js/
│   │   └── main.js          # Agent 2
│   └── images/
├── locale/                  # Agent 4: .po/.mo files
│   ├── en/
│   ├── ru/
│   └── uz/
├── fixtures/
│   └── initial_data.json    # Agent 4
├── media/                   # User uploads
├── manage.py
├── requirements.txt
└── .env.example
```

---

## 2. Model Contract (Agent 1 → Agents 3 & 4)

### Translation Field Pattern
All translatable models MUST follow this exact naming convention:
- Base field: `name`, `description`, `title`, `body`
- Russian: `name_ru`, `description_ru`, `title_ru`, `body_ru`
- Uzbek: `name_uz`, `description_uz`, `title_uz`, `body_uz`
- Future languages: `name_<lang>` where `<lang>` is the Django language code.

### Models

#### Category (`apps/products/models.py`)
```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, blank=True)
    name_uz = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_uz = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Categories'
```

#### Product (`apps/products/models.py`)
```python
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200, blank=True)
    name_uz = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200, blank=True)  # e.g. "Made with 100% real fruit"
    tagline_ru = models.CharField(max_length=200, blank=True)
    tagline_uz = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_uz = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    ingredients_ru = models.TextField(blank=True)
    ingredients_uz = models.TextField(blank=True)
    nutrition_facts = models.TextField(blank=True)
    nutrition_facts_ru = models.TextField(blank=True)
    nutrition_facts_uz = models.TextField(blank=True)
    weight_grams = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'name']
```

#### PageContent (`apps/core/models.py`) — for Story, Sustainability, generic pages
```python
class PageContent(models.Model):
    PAGE_CHOICES = [
        ('story', 'Our Story'),
        ('sustainability', 'Sustainability'),
    ]
    page_key = models.CharField(max_length=50, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200, blank=True)
    title_uz = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    subtitle_ru = models.CharField(max_length=300, blank=True)
    subtitle_uz = models.CharField(max_length=300, blank=True)
    body = models.TextField()  # Can store HTML
    body_ru = models.TextField(blank=True)
    body_uz = models.TextField(blank=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='pages/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### ContactMessage (`apps/core/models.py`)
```python
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
```

#### ContentBlock (`apps/cms/models.py`) — reusable CMS snippets
```python
class ContentBlock(models.Model):
    BLOCK_CHOICES = [
        ('home_hero', 'Homepage Hero'),
        ('home_story', 'Homepage Story Teaser'),
        ('home_featured', 'Homepage Featured Products'),
    ]
    block_key = models.CharField(max_length=50, choices=BLOCK_CHOICES, unique=True)
    title = models.CharField(max_length=200, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    title_uz = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_uz = models.TextField(blank=True)
    image = models.ImageField(upload_to='blocks/', blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
```

#### HeroSlide (`apps/cms/models.py`)
```python
class HeroSlide(models.Model):
    headline = models.CharField(max_length=200)
    headline_ru = models.CharField(max_length=200, blank=True)
    headline_uz = models.CharField(max_length=200, blank=True)
    subheadline = models.CharField(max_length=300, blank=True)
    subheadline_ru = models.CharField(max_length=300, blank=True)
    subheadline_uz = models.CharField(max_length=300, blank=True)
    cta_text = models.CharField(max_length=50, default='Learn More')
    cta_text_ru = models.CharField(max_length=50, blank=True)
    cta_text_uz = models.CharField(max_length=50, blank=True)
    cta_url = models.CharField(max_length=200, default='/products/')
    image = models.ImageField(upload_to='hero/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
```

---

## 3. Translation Utility Contract (Agent 4 → Agents 1, 3)

### File: `apps/translations/utils.py`
```python
from django.utils import translation

def get_translated_field(obj, field_name, lang=None):
    """
    Returns the translated value of `field_name` on `obj`.
    Falls back: requested lang → base field (no suffix).
    """
    if lang is None:
        lang = translation.get_language()
    if lang == 'en':
        return getattr(obj, field_name, '')
    translated = getattr(obj, f'{field_name}_{lang}', '')
    if translated:
        return translated
    return getattr(obj, field_name, '')
```

### Template Tag (Agent 4): `apps/translations/template_tags.py`
```python
from django import template
from apps.translations.utils import get_translated_field

register = template.Library()

@register.simple_tag
def trans_field(obj, field_name):
    return get_translated_field(obj, field_name)
```

Usage in templates: `{% trans_field product "name" %}`

---

## 4. URL Contract (Agent 3 + 4)

### Language Prefix
All URLs MUST be prefixed with language code: `/en/`, `/ru/`, `/uz/`
Default redirect: `/` → `/en/`

### URL Patterns (named routes)
```
/                    → redirect to /en/
/<lang>/             → HomeView                    name='home'
/<lang>/products/    → ProductListView             name='product_list'
/<lang>/products/<slug>/ → ProductDetailView         name='product_detail'
/<lang>/story/       → StoryView                   name='story'
/<lang>/sustainability/ → SustainabilityView       name='sustainability'
/<lang>/contact/     → ContactView                 name='contact'
```

### Root `config/urls.py`
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import LanguageRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LanguageRedirectView.as_view(), name='language_redirect'),
    path('<str:lang>/', include('apps.core.urls')),
    path('<str:lang>/products/', include('apps.products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

Note: `core/urls.py` handles `story/`, `sustainability/`, `contact/` under the `<lang>/` prefix.

---

## 5. Context Processor Contract (Agent 3)

### File: `apps/core/context_processors.py`
```python
def global_context(request):
    from apps.products.models import Category
    return {
        'brand_name': 'Biochem',  # Make overridable via settings later
        'nav_categories': Category.objects.filter(is_active=True).order_by('order'),
        'current_language': getattr(request, 'LANGUAGE_CODE', 'en'),
        'available_languages': [('en', 'English'), ('ru', 'Русский'), ('uz', 'O\'zbek')],
    }
```

Must be registered in `base.py`: `TEMPLATES[0]['OPTIONS']['context_processors']`

---

## 6. Static File Contract (Agent 2 → Agent 3)

Agent 2 creates pure HTML/CSS/JS in `frontend_prototype/`.
Agent 3 copies/moves these into Django's `static/` and `templates/` folders and adds `{% static %}` tags, `{% url %}`, `{% trans %}`, template blocks.

### CSS Variables (Agent 2 — exact variable names)
```css
:root {
  --color-bg: #F5F1E8;
  --color-bg-alt: #FFFFFF;
  --color-navy: #1A2B4A;
  --color-accent: #C9A96E;
  --color-text: #1A1A1A;
  --color-text-muted: #6B6B6B;
  --font-heading: 'Helvetica Neue', Arial, sans-serif;
  --font-body: 'Helvetica Neue', Arial, sans-serif;
  --font-accent: 'Georgia', 'Times New Roman', serif;
  --spacing-section: 100px;
  --spacing-unit: 8px;
}
```

These variable names are contractual. Agent 3 must keep them intact.

---

## 7. Settings Contract (Agent 1)

### `config/settings/base.py` must include:
- `INSTALLED_APPS`: `apps.core`, `apps.products`, `apps.cms`, `apps.translations`
- `LANGUAGE_CODE = 'en'`
- `LANGUAGES = [('en', 'English'), ('ru', 'Russian'), ('uz', 'Uzbek')]`
- `USE_I18N = True`
- `LOCALE_PATHS = [BASE_DIR / 'locale']`
- `STATIC_URL = '/static/'`, `STATICFILES_DIRS = [BASE_DIR / 'static']`
- `MEDIA_URL = '/media/'`, `MEDIA_ROOT = BASE_DIR / 'media'`
- `TEMPLATES` context processors must include `apps.core.context_processors.global_context`
- `MIDDLEWARE` must include `apps.translations.middleware.LocaleMiddleware` (inserted after `SessionMiddleware`)

### `.env.example`
```
DEBUG=True
SECRET_KEY=change-me-in-production
DATABASE_URL=postgres://user:password@localhost:5432/biochem
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 8. Admin Contract (Agent 1 + 4)

- ProductAdmin: list_display `name`, `category`, `is_featured`, `is_active`; list_filter `category`, `is_featured`; search_fields `name`, `name_ru`, `name_uz`
- Translation fields should be grouped using `fieldsets` with clear headers: `"English (Default)"`, `"Russian"`, `"Uzbek"`
- Example fieldset for Product:
```python
fieldsets = (
    (None, {'fields': ('category', 'slug', 'image', 'weight_grams', 'is_featured', 'is_active')}),
    ('English', {'fields': ('name', 'tagline', 'description', 'ingredients', 'nutrition_facts')}),
    ('Russian', {'fields': ('name_ru', 'tagline_ru', 'description_ru', 'ingredients_ru', 'nutrition_facts_ru')}),
    ('Uzbek', {'fields': ('name_uz', 'tagline_uz', 'description_uz', 'ingredients_uz', 'nutrition_facts_uz')}),
    ('SEO', {'fields': ('meta_title', 'meta_description')}),
)
```

---

## 9. Frontend Page List (Agent 2)

1. `index.html` — Homepage: hero section, 3 category cards, brand story teaser, featured products grid, footer
2. `products.html` — Product list: breadcrumb, category filter sidebar (or top tabs), 3-4 column product grid, pagination
3. `product-detail.html` — Large image left, info right, accordion for ingredients/nutrition, "Other Tastes" related products row
4. `story.html` — Hero banner, timeline/heritage sections, values grid
5. `sustainability.html` — Content-driven, image + text sections
6. `contact.html` — Split layout: contact form left, corporate info right

---

## 10. Bootstrap / Fixture Contract (Agent 4)

Provide `fixtures/initial_data.json` or `apps/core/management/commands/bootstrap.py` that creates:
- 3 Categories: "Fruit Juices", "Nectars", "Preserves" (with RU/UZ translations)
- 6-9 Products with names, descriptions, ingredients in EN/RU/UZ
- 1 PageContent for `story` and `sustainability`
- 2-3 HeroSlides
- 3 ContentBlocks for homepage sections

---

## 11. Commit Message Format (All Agents)

Use conventional commits scoped by app or layer:
- `feat(products): add Product and Category models`
- `feat(core): add homepage view and template`
- `feat(frontend): add responsive product grid`
- `feat(i18n): add translation utilities and middleware`
- `chore(config): split settings into base/local/production`
- `fix(admin): group translation fields in fieldsets`

---

**End of Contract.**
