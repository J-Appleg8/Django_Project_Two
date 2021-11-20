import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_two.settings")

import django

django.setup()


# Fake Pop Script
import random
from second_app.models import User
from faker import Faker

fakegen = Faker("en_GB")


def populate_users(n=5):
    for entry in range(n):

        # Create the fake data for that entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        # Create new User entry
        new_user = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=fake_email
        )[0]


if __name__ == "__main__":
    print("populating script!")
    populate_users(20)
    print("populating complete!")
