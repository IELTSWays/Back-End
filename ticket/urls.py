from django.urls import path
from ticket.views import TicketList

urlpatterns = [
    path("tickets", TicketList.as_view(), name="tickets"),
]


