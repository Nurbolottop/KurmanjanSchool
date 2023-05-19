from django.shortcuts import render

# my imports
from apps.base.models import Settings
from .models import Parents
# Create your views here.

def parents(request):
    setting = Settings.objects.latest("id")
    parent = Parents.objects.all()
    return render(request, "documents/parents.html",locals())
    