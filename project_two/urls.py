from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # Admin Path
    path("admin/", admin.site.urls),
    # Base App Path
    path("", include("second_app.urls")),
    # Alternate method
    # path("second_app/", include("second_app.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
