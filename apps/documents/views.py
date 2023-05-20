from django.shortcuts import render

# my imports
from apps.base.models import Settings
from .models import Parents,PublicLesson,LessonsForPublic
# Create your views here.

def parents(request):
    setting = Settings.objects.latest("id")
    parent = Parents.objects.all()
    return render(request, "documents/parents.html",locals())
    
def public_lessons(request):
    setting = Settings.objects.latest("id")
    lessons = LessonsForPublic.objects.all()
    return render(request, "documents/achyk_saat.html",locals())

def public_lessons_detail(request,id):
    setting = Settings.objects.latest("id")
    lessons = LessonsForPublic.objects.get(id =id)
    return render(request, "detail_pages/achyk_detail.html",locals())