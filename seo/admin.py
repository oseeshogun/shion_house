from django.contrib import admin
from .models import SEOImage

# Register your models here.

@admin.register(SEOImage)
class SEOImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'alt_text', 'created_at', 'updated_at')
    search_fields = ('title', 'alt_text', 'caption')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'alt_text', 'image', 'caption')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
