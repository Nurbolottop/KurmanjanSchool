from django.contrib import admin

# my imports
from .models import Parents
# Register your models here.
class ParentsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    
admin.site.register(Parents,ParentsFilterAdmin)
