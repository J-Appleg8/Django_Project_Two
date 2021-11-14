from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {"insert_me": "Hello I am from the views.py!"}
    return render(request, "second_app/index.html", context=my_dict)


def help(request):
    help_dict = {"help_me": "Help Page!"}
    return render(request, "second_app/help.html", context=help_dict)
