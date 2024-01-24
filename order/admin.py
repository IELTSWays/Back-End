from django.contrib import admin
from order.models import Order, ManualPayment


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'amount', 'user', 'status', 'created_at')
admin.site.register(Order, OrderAdmin)



class ManualPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'transaction_number', 'created_at')
    list_filter = ('user', 'order', 'created_at')
    search_fields = ['id', 'user', 'transaction_number','description']
admin.site.register(ManualPayment, ManualPaymentAdmin)