from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from .models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['new_url', 'old_url', 'user', 'created_at', 'last_access', 'code']
    fields = ['new_url', 'old_url', 'user', 'code', 'created_at', 'last_access']
    readonly_fields= ['created_at', 'last_access']
