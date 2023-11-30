from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from accounts.functions import get_user_data, login
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer, AdminUserSerializer, RegisterSerializer, AdminCreateUserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from accounts.views.permissions import IsAdmin
from accounts.models import User
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from accounts.functions import send_sms_create_user, send_sms_create_staff



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AdminLogin(APIView):
    permission_classes = []

    def post(self, *args, **kwargs):
        phone_number = self.request.data.get("phone_number")
        password = self.request.data.get("password")
        user = authenticate(phone_number=phone_number, password=password)
        if user is not None:
            access, refresh = login(user)
            data = {
                "refresh_token": refresh,
                #"access_token": access,
                "user_type": user.user_type,
                "user_data": UserSerializer(user).data}
            response = Response( {"success": True, "data": data}, status=status.HTTP_200_OK)
            response.set_cookie(
                "HTTP_ACCESS",
                f"Bearer {access}",
                max_age=ACCESS_TTL * 24 * 3600,
                secure=True,
                httponly=True,
                samesite="None",
            )
            return response

        else:
            return Response({"success": False, "errors": [_("Phone number or password is incorrect")]},status=status.HTTP_400_BAD_REQUEST)



class Admin(GenericAPIView):
    permission_classes = [IsAdmin]
    pagination_class = CustomPagination
    serializer_class = AdminUserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_type',]
    search_fields = ['name', 'phone_number', 'username']
    ordering_fields = ['id', 'created_at']

    def get(self, *args, **kwargs):
        users = self.filter_queryset(User.objects.all().order_by('-id').distinct())
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = AdminUserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AdminUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, *args, **kwargs):
        serializer = AdminCreateUserSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(phone_number=serializer.data['phone_number'])
            user.set_password(self.request.data['password'])
            user.save(update_fields=['password'])

            try:
                if user.user_type == "normal":
                    send_sms_create_user(user.phone_number, user.name, user.username, self.request.data['password'])
                else:
                    send_sms_create_staff(user.phone_number, user.name, user.username, self.request.data['password'])
            except:
                return Response({"success": False, "errors": [_("user create but error in sending sms")]},status=status.HTTP_400_BAD_REQUEST,)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



class AdminItem(APIView):
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdmin]

    def get(self, *args, **kwargs):
        user = User.objects.get(id=self.kwargs["id"])
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs["id"])
        serializer = AdminCreateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user.set_password(self.request.data['password'])
            user.save(update_fields=['password'])
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=self.kwargs["id"])
            user.delete()
            return Response("User deleted", status=status.HTTP_200_OK)
        except:
            return Response("Something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)


