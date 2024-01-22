from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'amount', 'user', 'status', 'created_at')
admin.site.register(Order, OrderAdmin)