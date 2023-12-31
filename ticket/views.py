from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ticket.serializers import GetTicketSerializer, CreatTicketSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from ticket.models import Ticket
from ticket import models

class Ticket(APIView):
    serializer_class = GetTicketSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        tickets = models.Ticket.objects.filter(user=self.request.user)
        serializer = self.serializer_class(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        req = self.request.data
        req['user'] = self.request.user.id
        serializer = CreatTicketSerializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TicketList(APIView):
    serializer_class = GetTicketSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        tickets = models.Ticket.objects.all()
        serializer = self.serializer_class(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class ticketItem(APIView):
    serializer_class = GetTicketSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        try:
            ticket = models.Ticket.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(ticket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("ticket not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)

