from django.urls import path

# my imports
from .views import pride_detail,gallery,gallery_detail,parlament

urlpatterns = [
    path('pride_detail/<int:id>/',pride_detail, name="pride_detail"),
    path('gallery', gallery, name="gallery"),
    path('gallery_detail/<int:id>/',gallery_detail, name="gallery_detail"),
    path('parlament', parlament, name="parlament"),
]