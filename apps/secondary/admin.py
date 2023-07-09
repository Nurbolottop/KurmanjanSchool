from django.contrib import admin

# my imports
from apps.base.models import Lessons
from .models import Slide,Pride,Data,Certificate,Gallery,GalleryDetail,Parlament,Student
# Register your models here.
class PrideFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
    
class LessonsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'number')
    search_fields = ('title', 'number')
    
# class ParlamentFilterAdmin(admin.ModelAdmin):
#     list_filter = ('name', )
#     list_display = ('name', )
#     search_fields = ('name', )
    
class StudentFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    
admin.site.register(Pride,PrideFilterAdmin)
admin.site.register(Slide)
admin.site.register(Data)
admin.site.register(Certificate)
admin.site.register(Gallery)
admin.site.register(GalleryDetail)
admin.site.register(Lessons,LessonsFilterAdmin)
# admin.site.register(Parlament,ParlamentFilterAdmin)
admin.site.register(Student,StudentFilterAdmin)






