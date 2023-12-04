from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from config.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("ticket/", include("ticket.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
