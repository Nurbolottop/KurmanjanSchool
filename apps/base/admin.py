from django.contrib import admin
from .models import Settings 
# Register your models here.

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
admin.site.register(Settings, SettingsFilterAdmin)