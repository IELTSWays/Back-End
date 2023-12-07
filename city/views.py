from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from city.serializers import ProvinceSerializer, CitySerializer
from rest_framework.permissions import AllowAny
from city.models import Province, City



class Provinces(APIView):
    serializer_class = ProvinceSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        province = Province.objects.all()
        serializer = self.serializer_class(province, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Cities(APIView):
    serializer_class = CitySerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        city = City.objects.all()
        serializer = self.serializer_class(city, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)