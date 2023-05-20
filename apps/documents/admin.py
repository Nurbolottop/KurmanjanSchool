from django.contrib import admin

# my imports
from .models import Parents,LessonsForPublic,PublicLesson
# Register your models here.
class ParentsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )

class PublicLessonFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    
admin.site.register(Parents,ParentsFilterAdmin)
admin.site.register(LessonsForPublic)
admin.site.register(PublicLesson,PublicLessonFilterAdmin)

