from django.contrib import admin
from .models import ContentBlock, HeroSlide


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('block_key', 'title', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'title_ru', 'title_uz')
    fieldsets = (
        (None, {'fields': ('block_key', 'image', 'order', 'is_active')}),
        ('English (Default)', {'fields': ('title', 'body')}),
        ('Russian', {'fields': ('title_ru', 'body_ru')}),
        ('Uzbek', {'fields': ('title_uz', 'body_uz')}),
    )


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('headline', 'cta_text', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('headline', 'headline_ru', 'headline_uz')
    fieldsets = (
        (None, {'fields': ('image', 'cta_url', 'order', 'is_active')}),
        ('English (Default)', {'fields': ('headline', 'subheadline', 'cta_text')}),
        ('Russian', {'fields': ('headline_ru', 'subheadline_ru', 'cta_text_ru')}),
        ('Uzbek', {'fields': ('headline_uz', 'subheadline_uz', 'cta_text_uz')}),
    )
