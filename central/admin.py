from django.contrib import admin ,messages
from .models import WebsiteSetting,Slider,FAQs ,Blog

def active_status(modelAdmin, request, queryset):
    """ messages.success -> shows green alert """
    """ messages.error -> shows red alert """
    """ messages.warning -> shows brown alert """
    """ messages.info -> shows green alert """
    try:
        queryset.update(status=True)
        messages.success(request, 'Selected record(s) marked as active')
    except Exception as e:
        messages.error(request, str(e))

def inactive_status(modelAdmin, request, queryset):
    try:
        queryset.update(status=False)
        messages.success(request, 'Selected record(s) marked as active')
    except Exception as e:
        messages.error(request, str(e))

class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone',]


admin.site.register(WebsiteSetting, WebsiteSettingAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['heading', 'sub_heading', 'image', 'status']
    list_filter = ['heading']
    search_fields = ['heading']


admin.site.register(Slider, SliderAdmin)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ['title'] }
    list_display = ['title', 'date_time', 'status']
    list_filter = ['title']
    search_fields = ['title']


admin.site.register(Blog, BlogAdmin)


class FAQsAdmin(admin.ModelAdmin):
    list_display = ['question']
    list_filter = ['question']
    search_fields = ['question']


admin.site.register(FAQs, FAQsAdmin)
