from django.urls import path

# my imports
from .views import parents

urlpatterns = [
    path('parents',parents, name="parents")
]