from django.urls import path
from city.views import Provinces, Cities

urlpatterns = [
    path("provinces", Provinces.as_view(), name="provinces"),
    path("cities", Cities.as_view(), name="cities"),
]


