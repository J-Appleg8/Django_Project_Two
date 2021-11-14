from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "second_app"

urlpatterns = [
    # Homepage View
    path("", views.index, name="index"),
    path("help/", views.help, name="help"),
]
