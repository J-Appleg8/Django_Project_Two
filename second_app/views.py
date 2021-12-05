from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord, User
from .forms import NewUserForm


def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": webpages_list}

    return render(request, "second_app/index.html", context=date_dict)


def user_data(request):
    form = NewUserForm()

    if request.method == "POST":

        # If the request method is POST then we pass in the request.POST
        form = NewUserForm(request.POST)

        # If the form is valid then we will save the data to the database
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error: Form Invalid")

    return render(request, "second_app/users.html", context={"form": form})

    # userdata_list = User.objects.order_by("first_name")
    # user_dict = {"user_list": userdata_list}

    # return render(request, "second_app/users.html", context=user_dict)
