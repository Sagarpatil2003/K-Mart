from django.contrib import admin
from cart.models import Cart



class CartAdmin(admin.ModelAdmin):
   list_display = ['user', 'product', 'variation', 'quantity']
   list_filter = ['user', 'product']
   search_fields = ['user__first_name']


admin.site.register(Cart, CartAdmin)
