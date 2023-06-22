from django.contrib import admin ,messages
from . models import Brand

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


class BrandAdmin(admin.ModelAdmin):
   list_display = ['name', 'status']
   list_filter = ['status']
   search_fields = ['name']


admin.site.register(Brand, BrandAdmin)


