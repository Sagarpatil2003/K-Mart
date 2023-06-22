from django.contrib import admin, messages
from order.models import Order, OrderDetails



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

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "mobile", "payment", "status"]
    list_filter = ["status", "payment"]
    search_fields = ["id", "user__first_name"]
    inlines = (OrderDetailsInline, )


admin.site.register(Order, OrderAdmin)
