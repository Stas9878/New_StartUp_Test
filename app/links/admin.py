from django.contrib import admin
from .models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    '''Конфиг для оттображения Links в админ - панели'''

    list_display = ['new_url', 'old_url', 'user', 'created_at', 'last_access', 'code']
    fields = ['new_url', 'old_url', 'user', 'code', 'created_at', 'last_access']
    readonly_fields= ['created_at', 'last_access']
