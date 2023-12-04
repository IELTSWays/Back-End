from django.urls import path
from ticket.views import Ticket, TicketList

urlpatterns = [
    path("tickets", Ticket.as_view(), name="tickets"),
    path("ticket-list", TicketList.as_view(), name="ticket-list"),
]


