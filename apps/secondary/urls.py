from django.urls import path

# my imports
from .views import pride_detail

urlpatterns = [
    path('pride_detail/<int:id>/',pride_detail, name="pride_detail")
]