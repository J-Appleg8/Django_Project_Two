from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Webpage, AccessRecord, User


def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": webpages_list}

    return render(request, "second_app/index.html", context=date_dict)


def user_data(request):
    userdata_list = User.objects.order_by("first_name")
    user_dict = {"user_list": userdata_list}

    return render(request, "second_app/users.html", context=user_dict)
