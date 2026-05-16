from django.db import models


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

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.get_block_key_display()


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

    def __str__(self):
        return self.headline
