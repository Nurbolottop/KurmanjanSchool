from django.shortcuts import render

# my imports
from apps.base.models import Settings
from .models import Institutional,InstitutionalDetail,Software,SoftwareDetail
# Create your views here.
def institunional(request):
    setting = Settings.objects.latest("id")
    accreditation = Institutional.objects.all()
    return render(request, "documents/inst_akred.html",locals())

def institunional_detail(request,id):
    setting = Settings.objects.latest("id")
    accreditation = Institutional.objects.get(id = id)
    return render(request, "detail_pages/inst_detail.html",locals())

def software(request):
    setting = Settings.objects.latest("id")
    accreditation = Software.objects.all()
    return render(request, "documents/prog_akred.html",locals())

def software_detail(request,id):
    setting = Settings.objects.latest("id")
    accreditation = Software.objects.get(id = id)
    return render(request, "detail_pages/prog_detail.html",locals())