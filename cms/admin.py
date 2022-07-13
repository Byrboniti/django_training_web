from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider
# Register your models here.

class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title',  'cms_css', 'get_img', 'cms_text', )
    list_display_links = ('cms_title',)
    list_editable = ('cms_css', )
    fields = ('cms_title',  'cms_css', 'get_img', 'cms_text',)
    readonly_fields = ("get_img",)
    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'No img'
    get_img.short_description = 'Миниатюра'

admin.site.register(CmsSlider, CmsAdmin)