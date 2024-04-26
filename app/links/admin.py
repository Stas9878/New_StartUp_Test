from django.contrib import admin
from .models import Links

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    pass

        
