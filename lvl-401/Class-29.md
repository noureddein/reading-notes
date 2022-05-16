# Django Custom User

## Django Best Practices
  - The official Django documentation highly recommends to use a custom user model for all new Django projects. 

## AbstractUser vs AbstractBaseUser
  - Use `AbstractUser` or `AbstractBaseUser` to create a custom user model.
  - Inherit one of thess classes to start create your model.

## Create Custom user model
  - First install Django and create new app called **accounts**
  - Update your django setting, and add the **accounts** app to it.
  - Then at the bottom of the entire file, add a new variable to your settings called **AUTH_USER_MODEL** and assign to it this value **"accounts.CustomUser"**. `AUTH_USER_MODEL = "accounts.CustomUser"`
  - From the `models.py` file, create new class called `CustomUser`, the class must be inherited from `AbstractUser`
```python
    # accounts/models.py
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class CustomUser(AbstractUser):
        pass
        # add additional fields in here

        def __str__(self):
            return self.username
```
  - Create a new file in the accounts app folder called `forms.py`
  - Add the bellow code snippet
```python
    # accounts/forms.py
    from django import forms
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    from .models import CustomUser

    class CustomUserCreationForm(UserCreationForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")

    class CustomUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")
```
  - Finally add the bellow code snippet to the `admin.py` 
```python
    # accounts/admin.py
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from .forms import CustomUserCreationForm, CustomUserChangeForm
    from .models import CustomUser

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ["email", "username",]

    admin.site.register(CustomUser, CustomUserAdmin)
```
  - Now we need to run these two commands in the terminal:
    - `python manage.py makemigrations accounts`
    - `python manage.py migrate`
  - And you will need to create the supper user, run this command and follow the steps:
    - `python manage.py createsuperuser`


## Templates/Views/URLs
  - Now we need to create a homepage with these links **log in**, **log out**, and **sign up**.
  - Create a template folder at the project-level and add the following:
    - Create a new folder called `registration` and add these two html files
      - `login.html`
      - `signup.html`
    - At the template root add these two html files:
      - `base.html`
      - `home.html`
  - Update the files with the code bellow:
```html
    <!-- templates/base.html -->
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title><!-- Add block title  --></title>
    </head>
    <body>
    <main>
        <!--Add block content -->
    </main>
    </body>
    </html>
```

```html
    <!-- templates/home.html -->
    <!--  extends "base.html"  -->

    <!-- { block title }Home{ endblock } -->

    { block content }
    { if user.is_authenticated }
    Hi {{ user.username }}!
    <p><a href="{ url 'logout' }">Log Out</a></p>
    { else }
    <p>You are not logged in</p>
    <a href="{ url 'login' }">Log In</a> |
    <a href="{ url 'signup' }">Sign Up</a>
    { endif }
    { endblock }
```

```html
    <!-- templates/registration/login.html -->
    { extends "base.html" }

    { block title }Log In{ endblock }

    { block content }
    <h2>Log In</h2>
    <form method="post">
    { csrf_token }
    {{ form.as_p }}
    <button type="submit">Log In</button>
    </form>
    { endblock }
```
```html
    <!-- templates/registration/signup.html -->
    { extends "base.html" }

    { block title }Sign Up{ endblock }

    { block content }
    <h2>Sign Up</h2>
    <form method="post">
    { csrf_token }
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
    </form>
    { endblock }
```
  - Update the `setting.py`
```python
    # django_project/settings.py
    TEMPLATES = [
        {
            ...
            "DIRS": [BASE_DIR / "templates"],  # new
            ...
        },
    ]
```
  - Set the redirect for log in and log out by adding the two variables to the `setting.py` file:
    - `LOGIN_REDIRECT_URL = "home"`
    - `LOGOUT_REDIRECT_URL = "home"`
  - In the project urls, update the `urlpatterns` variable:

```python
    # django_project/urls.py
    from django.contrib import admin
    from django.urls import path, include
    from django.views.generic.base import TemplateView

    urlpatterns = [
        path("", TemplateView.as_view(template_name="home.html"), name="home"),
        path("admin/", admin.site.urls),
        path("accounts/", include("accounts.urls")),
        path("accounts/", include("django.contrib.auth.urls")),
    ]
```
  - At the `accounts` app folder create a `urls.py` file, and fill it with the bellow code snippet
```python
# accounts/urls.py
from django.urls import path

from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
```
  - Final step, update the `view.py` with the following code:
```python
    # accounts/views.py
    from django.urls import reverse_lazy
    from django.views.generic.edit import CreateView

    from .forms import CustomUserCreationForm

    class SignUpView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy("login")
        template_name = "registration/signup.html"
```
  - Now, fire up the server and check the work!!