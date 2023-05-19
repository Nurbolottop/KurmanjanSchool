from django.contrib import admin
from .models import Slide,Pride,Data
# Register your models here.
class PrideFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
    
admin.site.register(Pride,PrideFilterAdmin)
admin.site.register(Slide)
admin.site.register(Data)
