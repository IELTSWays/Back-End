from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from config.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path("admin/", admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("accounts/", include("accounts.urls")),
    path("ticket/", include("ticket.urls")),
    path("city/", include("city.urls")),
    path("book/", include("book.urls")),
    path("exam/", include("exam.urls")),
    path("answer/", include("answers.urls")),
    path("cart/", include("cart.urls")),
    path("payment/", include("payment.urls")),
    path("teacher/", include("teacher.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
