from django.urls import path
from . import views

app_name = "second_app"

urlpatterns = [
    # Homepage View
    path("", views.index, name="index"),
    path("users/", views.user_data, name="user_data"),
]
