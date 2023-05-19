from django.contrib import admin
# my imports
from .models import Settings,About
# Register your models here.

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
admin.site.register(Settings, SettingsFilterAdmin)
admin.site.register(About, AboutFilterAdmin)
