from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = 'biochem/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.filter(is_active=True).select_related('category')
        category_slug = self.kwargs.get('slug')
        if category_slug:
            self.current_category = get_object_or_404(Category, slug=category_slug, is_active=True)
            qs = qs.filter(category=self.current_category)
        else:
            self.current_category = None
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.filter(is_active=True)
        ctx['current_category'] = getattr(self, 'current_category', None)
        return ctx


class ProductDetailView(DetailView):
    model = Product
    template_name = 'biochem/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Product.objects.filter(is_active=True).select_related('category')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product = self.object
        ctx['related_products'] = (
            Product.objects
            .filter(category=product.category, is_active=True)
            .exclude(pk=product.pk)
            .order_by('?')[:4]
        )
        return ctx
