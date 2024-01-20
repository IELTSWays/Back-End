from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from config.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from . import views
from oauth.views import GoogleLoginView, UserRedirectView


urlpatterns = [
    path('', views.index, name='home'),
    path("auth/google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("redirect/", UserRedirectView.as_view(), name="redirect"),
    path("admin/", admin.site.urls),
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
