from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.products.models import Category, Product
from apps.cms.models import ContentBlock, HeroSlide
from apps.core.models import PageContent, ContactMessage
from .forms import ContactForm


class LanguageRedirectView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/en/')


class HomeView(TemplateView):
    template_name = 'biochem/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['slides'] = HeroSlide.objects.filter(is_active=True)
        ctx['featured_products'] = Product.objects.filter(is_featured=True, is_active=True)[:6]
        ctx['categories'] = Category.objects.filter(is_active=True)
        try:
            ctx['story_teaser'] = ContentBlock.objects.get(block_key='home_story', is_active=True)
        except ContentBlock.DoesNotExist:
            ctx['story_teaser'] = None
        return ctx


class StoryView(TemplateView):
    template_name = 'biochem/story.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            ctx['page'] = PageContent.objects.get(page_key='story')
        except PageContent.DoesNotExist:
            ctx['page'] = None
        return ctx


class SustainabilityView(TemplateView):
    template_name = 'biochem/sustainability.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            ctx['page'] = PageContent.objects.get(page_key='sustainability')
        except PageContent.DoesNotExist:
            ctx['page'] = None
        return ctx


class ContactView(View):
    template_name = 'biochem/contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': ContactForm()})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data.get('phone', ''),
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, _('Thank you for your message. We will be in touch soon.'))
            form = ContactForm()
        return render(request, self.template_name, {'form': form})
