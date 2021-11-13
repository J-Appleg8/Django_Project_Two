# <span style="color:khaki">Django Project:</span>

A Django Project is a collection of applications and configurations that, when combined together, will make up the full web application

# <span style="color:khaki">Django App:</span>

## <span style="color:lemonchiffon">Overview:</span>

A Django Application is created to perform a particular functionality for your entire web application

- **Example:** Registration app, polling app, comments app etc.

- These Django Apps can then be plugged into other Django Projects, so you can reuse them

The main architectural design pattern employed by Django is:

1. Model
1. View
1. Template

![alt text](Django_Architecture.png "Title")

## <span style="color:lemonchiffon">Django App Files:</span>

- \_\_init\_\_.py
  - This is a blank Python script that, due to its special name, let's Python know that this directory can be treated as a package
- `admin.py`
  - You can register your models here which Django will then use in the Django admin interface
- `apps.py`
  - Here you can place application specific configurations
- `models.py`
  - Place to store the applicatiion's data models
- `tests.py`
  - Here you can store a series of functions to test out your application's code
- `views.py`
  - This is where you have functions that handle requests and return responses
  - Each view must return a response
- migrations folder
  - Directory that stores database specific information as it relates to the models
  - A migration allows you to move databases from one design to another
    - This is also reversible

## <span style="color:lemonchiffon">URL Mapping:</span>

- The `include()` function allows us to look for a match with regular expressions and link back to our application's own `urls.py` file

- We would add the following to the project's urls.py:

```python
from django.urls import path, include

urlpatterns = [
  path("", include("first_app.urls")),
]
```

OR

```python
from django.urls import url, include

urlpatterns = [
  url(r"^$", include("first_app.urls")),
]
```
