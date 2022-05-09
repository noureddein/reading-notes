# Django Models
## Overview 
  - Models used to draw the staructure of stored data.
  - With models we can define the data type of each field.
  - With models we don't need to talk directly to the database, Django will take the dirty work for us.

## Designing the LocalLibrary models
  - Best practices to designing a models is separate models for every "object" (a group of related information.
  - <image src='./class-27-img/local_library_model_uml.svg' style = 'width:47rem;'>
  - The image above shows how we can separate models, so each table will be responsible for one specific thing.
  
## Model primer
### Model definition
  - Models defined in `models.py` file.
  - Models should be inherited from the `django.db.models.Model`
  - Each attribute of the model represents a database field.
  - Ex: Assume we have an app called **myapp** this app have a class in the `models.py` as the bellow code:

```python
    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
```
  - The code above will create a table in the database with columns type as the bellow code:
  - The table name will be `myapp_person`
```SQL
  CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

  - COMMON FIELD ARGUMENTS:
    - help_text
    - verbose_name
    - default
    - null
    - blank
    - choices
    - primary key
  - COMMON FIELD TYPES
    - CharField
    - TextField
    - IntegerField
    - DateField and DateTimeField
    - EmailField
    - ManyToManyField
    - ForeignKey
    - AutoField
  
### Metadata
  - Meta class used to control the default ordering of records returned when you query the model type.
  - Ex:
```python
    class Meta:
    ordering = ['-my_field_name']
```