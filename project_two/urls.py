from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin Path
    path("admin/", admin.site.urls),
    # Base App Path
    path("", include("second_app.urls")),
    # Alternate method
    path("second_app/", include("second_app.urls")),
]
