from django.contrib import admin

# my imports
from .models import Institutional,InstitutionalDetail,Software,SoftwareDetail
# Register your models here.

class InstitutionalFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )

class InstitutionalDetailFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    
class SoftwareFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    
class SoftwareDetailFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    
admin.site.register(Institutional,InstitutionalFilterAdmin)
admin.site.register(InstitutionalDetail,InstitutionalDetailFilterAdmin)
admin.site.register(Software,SoftwareFilterAdmin)
admin.site.register(SoftwareDetail,SoftwareDetailFilterAdmin)
