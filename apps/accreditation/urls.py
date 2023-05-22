from django.urls import path

# my imports
from .views import institunional,institunional_detail,software,software_detail

urlpatterns = [
    path('institunional/accreditation/', institunional, name="institunional"),
    path('institunional/accreditation/<int:id>/', institunional_detail, name="institunional_detail"),
    path('software/accreditation/', software, name="software"),
    path('software/accreditation/<int:id>/', software_detail, name="software_detail"),
]