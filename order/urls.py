from django.urls import path
from ticket.views import Ticket, TicketList, ticketItem

urlpatterns = [
    path("tickets", Ticket.as_view(), name="tickets"),
    path("ticket-list", TicketList.as_view(), name="ticket-list"),
    path('ticket-item/<int:id>', ticketItem.as_view(), name='ticket-item'),
]


