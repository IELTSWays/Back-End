from django.contrib import admin
from ticket.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
admin.site.register(Ticket, TicketAdmin)

