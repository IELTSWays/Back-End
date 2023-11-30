from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from config.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("admin-panel/", include("admin_panel.urls")),
    path("letters/", include("letter.urls")),
    path("invoices/", include("invoice.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
