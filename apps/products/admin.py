from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'name_ru', 'name_uz')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {'fields': ('slug', 'image', 'order', 'is_active')}),
        ('English (Default)', {'fields': ('name', 'description')}),
        ('Russian', {'fields': ('name_ru', 'description_ru')}),
        ('Uzbek', {'fields': ('name_uz', 'description_uz')}),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'name_ru', 'name_uz')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('category', 'slug', 'image', 'weight_grams', 'is_featured', 'is_active'),
        }),
        ('English (Default)', {
            'fields': ('name', 'tagline', 'description', 'ingredients', 'nutrition_facts'),
        }),
        ('Russian', {
            'fields': ('name_ru', 'tagline_ru', 'description_ru', 'ingredients_ru', 'nutrition_facts_ru'),
        }),
        ('Uzbek', {
            'fields': ('name_uz', 'tagline_uz', 'description_uz', 'ingredients_uz', 'nutrition_facts_uz'),
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
        }),
    )
