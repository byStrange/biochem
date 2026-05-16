from django.contrib import admin
from .models import PageContent, ContactMessage


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page_key', 'title', 'updated_at')
    search_fields = ('title', 'title_ru', 'title_uz')
    fieldsets = (
        (None, {'fields': ('page_key', 'hero_image')}),
        ('English (Default)', {'fields': ('title', 'subtitle', 'body')}),
        ('Russian', {'fields': ('title_ru', 'subtitle_ru', 'body_ru')}),
        ('Uzbek', {'fields': ('title_uz', 'subtitle_uz', 'body_uz')}),
        ('SEO', {'fields': ('meta_title', 'meta_description')}),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
    fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at', 'is_read')
