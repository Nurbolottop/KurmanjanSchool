from django.contrib import admin
from django.contrib.auth.models import User, Group

# my imports

from .models import Settings,About,New,Teacher,Contact,History
# Register your models here.

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class HistoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('year', )
    list_display = ('year', 'descriptions')
    search_fields = ('year', 'descriptions')

class NewFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class TeacherFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )

class СontactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'message')
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    
# Deleting Models <<User>> and <<Group>>
admin.site.unregister(User)
admin.site.unregister(Group) 
admin.site.register(Settings, SettingsFilterAdmin)
admin.site.register(About, AboutFilterAdmin)
admin.site.register(History, HistoryFilterAdmin)
admin.site.register(New, NewFilterAdmin)
admin.site.register(Teacher, TeacherFilterAdmin)
admin.site.register(Contact, СontactFilterAdmin)


