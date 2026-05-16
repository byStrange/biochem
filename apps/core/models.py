from django.db import models


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
    body = models.TextField()
    body_ru = models.TextField(blank=True)
    body_uz = models.TextField(blank=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='pages/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['page_key']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
