# Permissions & Postgresql

## Authentication classes
There is two types of classes for authentication in Django REST framework
  - **IsAuthenticated**
    - IsAuthenticated is the simplest style of authentication, with this class we can give the user the permission to access the data or not.
  - **IsAuthenticatedOrReadOnly**
    - With IsAuthenticatedOrReadOnly class we can give the user full access or a basic level of accessability which is reading only.


## Where to check if user authenticated or Not?
  - We always check if the user authenticated or not at the very top of the view.
  - The logic of authentication should be done before executing any code of the view.


## What response should be returned when checks fails?
  - The request was successfully authenticated, but permission was denied. — An HTTP 403 Forbidden response will be returned.
  - The request was not successfully authenticated, and the highest priority authentication class does not use WWW-Authenticate headers. — An HTTP 403 Forbidden response will be returned.
  - The request was not successfully authenticated, and the highest priority authentication class does use WWW-Authenticate headers. — An HTTP 401 Unauthorized response, with an appropriate WWW-Authenticate header will be returned.


## Permissions Levels
We can apply permissions for:
  - Project-level
  - View-level
  - Object-level

## Object level permissions
  - Object level permissions should give the user a permission to act on a specific particular object which will typically be a model instance.
  - Object level permissions runs by generic view when `.get_object()`.
  - If the user is not allowed to act on object, an `exceptions.PermissionDenied` exception will be raised.

## Setting the permission policy
The default permission policy may be set globally, using the DEFAULT_PERMISSION_CLASSES setting
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```
If we did not specified the permissions, the setting defaults will be allowing unrestricted access:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

You can also set the authentication policy on a per-view, or per-viewset basis, using the APIView class-based views.

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
```
> Note: when you set new permission classes via the class attribute or decorators you're telling the view to ignore the default list set in the settings.py file.

> Every time we created a new model by default Django builds four different permissions. 
## Project-level permissions  
  - ### **AllowAny**
    - The **AllowAny** permission class will allow unrestricted access, so anyone can access the data.
  - ### **IsAuthenticated**
    - The IsAuthenticated permission class will deny permission to any unauthenticated user, and allow permission otherwise.
    - This permission is suitable if you want your API to only be accessible to registered users
  - ### **IsAdminUser**
    - The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.
    - This permission is suitable if you want your API to only be accessible to a subset of trusted administrators.
  - ### **IsAuthenticatedOrReadonly**
    - The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request. Requests for unauthorised users will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.
    - This permission is suitable if you want to your API to allow read permissions to anonymous users, and only allow write permissions to authenticated users.

## View level permissions
  - ### **DjangoModelPermissions**
    - This permission class ties into Django's standard `django.contrib.auth` model permissions. This permission must only be applied to views that have a `.queryset` property or `get_queryset()` method. Authorization will only be granted if the user is authenticated and has the relevant model permissions assigned.
      - `POST` requests require the user to have the `add` permission on the model.
      - `PUT` and PATCH requests require the user to have the change permission on the model.
      - `DELETE` requests require the user to have the delete permission on the model.
    - The default behaviour can also be overridden to support custom model permissions. For example, you might want to include a view model permission for GET requests.

    - To use custom model permissions, override `DjangoModelPermissions` and set the `.perms_map` property. Refer to the source code for details.

  - ### **DjangoModelPermissionsOrAnonReadOnly**
    - Similar to DjangoModelPermissions, but also allows unauthenticated users to have read-only access to the API.

---

### Resources:
  1. [Very Academy](https://www.youtube.com/watch?v=5AOn0BmSXyE)
  2. [Django REST Framework docs](https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy)