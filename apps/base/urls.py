from django.urls import path
# my imports
from .views import index

urlpatterns = [
    path('', index, name="index"),
]