from django.urls import path
# my imports
from .views import index,about,contact

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    
]