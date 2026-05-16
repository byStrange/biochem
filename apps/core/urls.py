from django.urls import path
from .views import HomeView, StoryView, SustainabilityView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('story/', StoryView.as_view(), name='story'),
    path('sustainability/', SustainabilityView.as_view(), name='sustainability'),
    path('contact/', ContactView.as_view(), name='contact'),
]
