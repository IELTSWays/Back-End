from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from config import responses
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from letter.models import Letter
from letter.serializers import LetterSerializer
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer


class OverView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        user=self.request.user

        data = {
            "user_id": user.id,
            "name": user.name,
            "user_type": user.user_type,
            "phone_number": user.phone_number,
            "factors_count": Invoice.objects.filter(user=user,status="پرداخت نشده").count(),
            "letters_count": Letter.objects.filter(user=user).count(),
            "factors": InvoiceSerializer(Invoice.objects.filter(user=user,status="پرداخت نشده"),many=True).data,
            "letters": LetterSerializer(Letter.objects.filter(user=user),many=True).data,
        }

        return Response({"success": True,"data": data,},status=status.HTTP_200_OK)