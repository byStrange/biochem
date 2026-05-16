from django.db import models


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

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200, blank=True)
    name_uz = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200, blank=True)
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

    def __str__(self):
        return self.name
