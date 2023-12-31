from django.contrib import admin
from payment.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'amount', 'success', 'created_at')
admin.site.register(Transaction, TransactionAdmin)