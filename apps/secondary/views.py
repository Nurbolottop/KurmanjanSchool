from django.shortcuts import render
from apps.base.models import Settings
from .models import Pride
# Create your views here.
def pride_detail(request,id):
    setting = Settings.objects.latest("id")
    pride = Pride.objects.get(id =id)
    
    return render(request, "detail_pages/pride_detail.html",locals())