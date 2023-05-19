from django.urls import path
# my imports
from .views import index,about,contact,news,news_detail

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('news/', news, name="news"),
    path('news_detail/<int:id>/', news_detail, name="news_detail"),
    
]