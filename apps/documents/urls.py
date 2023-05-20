from django.urls import path

# my imports
from .views import parents,public_lessons,public_lessons_detail

urlpatterns = [
    path('parents',parents, name="parents"),
    path('public_lessons', public_lessons, name="public_lessons"),
    path('public_lessons_detail/<int:id>/',public_lessons_detail, name="public_lessons_detail"),
]