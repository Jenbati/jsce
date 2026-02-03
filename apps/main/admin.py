from django.contrib import admin
from .models import Volume, Article
from django import forms

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('formatted_volume', 'formatted_date', 'cover_image_preview')
    search_fields = ('number',)
    ordering = ('-number',)

    def formatted_volume(self, obj):
        return f"Volume {obj.number}"
    formatted_volume.short_description = "Volume"

    def formatted_date(self, obj):
        return f"({obj.date.strftime('%B %Y')})"
    formatted_date.short_description = "Date"

    def cover_image_preview(self, obj):
        if obj.cover_image:
            return f"<img src='{obj.cover_image.url}' width='60' height='80' style='object-fit:cover;' />"
        return "No Image"
    cover_image_preview.allow_tags = True
    cover_image_preview.short_description = "Cover"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'volume', 'page_start', 'page_end')
    search_fields = ('title', 'authors', 'keywords')
    list_filter = ('volume',)
    ordering = ('volume', 'page_start')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].widget = forms.TextInput(attrs={'size': 130})
        form.base_fields['keywords'].widget = forms.TextInput(attrs={'size': 100})
        form.base_fields['authors'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 140})
        return form