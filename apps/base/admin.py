from django.contrib import admin
from django.contrib.auth.models import User, Group

# my imports
from .models import Settings,About,New
# Register your models here.

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class NewFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

# Deleting Models <<User>> and <<Group>>
admin.site.unregister(User)
admin.site.unregister(Group) 
admin.site.register(Settings, SettingsFilterAdmin)
admin.site.register(About, AboutFilterAdmin)
admin.site.register(New, NewFilterAdmin)
