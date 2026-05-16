from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<slug:slug>/', ProductListView.as_view(), name='product_list_category'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
