from django.contrib import admin, messages
from django.db import models
from brand.models import Brand
from django.template.defaultfilters import slugify
from .models import product_category, Product, ProductVariation, ProductTag, ProductImage

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
        messages.success(request, 'Selected record(s) marked as inactive')
    except Exception as e:
        messages.error(request, str(e))

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'show_on_homepage']
    list_filter = ['status', 'show_on_homepage']
    search_fields = ['name']
    actions = [active_status, inactive_status]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_category', 'brand', 'price', 'status']
    list_filter = ['product_category', 'brand', 'status']
    search_fields = ['name', 'description']
    actions = [active_status, inactive_status]

class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    search_fields = ['name']
    actions = [active_status, inactive_status]

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    search_fields = ['name']
    actions = [active_status, inactive_status]

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']

admin.site.register(product_category, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
admin.site.register(ProductTag, ProductTagAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
