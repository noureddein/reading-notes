# Intro to Django

## Object-relational mapper
```
    class Band(models.Model):
        """A model of a rock band."""
        name = models.CharField(max_length=200)
        can_rock = models.BooleanField(default=True)

    class Member(models.Model):
        """A model of a rock band member."""
        name = models.CharField("Member's name", max_length=200)
        instrument = models.CharField(choices=(
                ('g', "Guitar"),
                ('b', "Bass"),
                ('d', "Drums"),
            ),
            max_length=1
        )
        band = models.ForeignKey("Band")
```
  - As we can see in the above code, in Django we can define the table and it's fields using python classes.
  - So the code can be more readable and maintainable.

## URLs and views
```
    from django.urls import path

    from . import views

    urlpatterns = [
        path('bands/', views.band_listing, name='band-list'),
        path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
        path('bands/search/', views.band_search, name='band-search'),
    ]
```
  - The code above shows *band* app with all the URLs that related to it.
  - Django designed to make urls cleaner and elegant.
  - Each app has it's own URLs module.

## Templates
```
    <html>
    <head>
        <title>Band Listing</title>
    </head>
    <body>
        <h1>All Bands</h1>
        <ul>
        {% for band in bands %}
        <li>
            <h2><a href="{{ band.get_absolute_url }}">{{ band.name }}</a></h2>
            {% if band.can_rock %}<p>This band can rock!</p>{% endif %}
        </li>
        {% endfor %}
        </ul>
    </body>
    </html>
```
  - The pice of code above shows the DTL (Django Template Languge).
  - Django templates designed to make the front-end code extensible and fixable.

## Forms
```
    from django import forms

    class BandContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField()
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)
```
  - Django provides a powerful form library that handles rendering forms as HTML.
  - Django validate user inputs automatically.
  - Django convert user inputs to the native Python data type automatically.

## Authentication

```
    from django.contrib.auth.decorators import login_required
    from django.shortcuts import render

    @login_required
    def my_protected_view(request):
        """A view that can only be accessed by logged-in users"""
        return render(request, 'protected.html', {'current_user': request.user})
```

  - Django comes with a full-featured and secure authentication system.
  - It handles user accounts, groups, permissions and cookie-based user sessions

## Admin
  - Django provides an admin page that can control the whole project and database.
---
# How Django Works Behind the Scenes
  - Django is an open source, mean the code is available for free on Github.
  - As with all open source projects, the two major issues that crop up are **funding** and **control**.
  - There are a host of decidedly tasks needed to maintain and sustain an open source project:
    - Handling any legal/trademark issues.
    - Triaging tickets.
    - Guiding community discussions.
    - Organizing conferences.
    - Managing releases
  -  Typically funding involved in one of three forms:
     -  Corporate Sponsor
     -  Solo - An individual developer initially creates code, open sources it, and retains default control.
     -  Non-profit - This was Django’s approach early on, in 2008, when the Django Software Foundation was formed to promote, support, and advance Django.
  -  Django keeps updated by two paid members, and with other volunteers.