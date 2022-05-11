# Django CRUD and Forms

## HTML Forms
```HTML
    <form action="/team_name_url/" method="post">
        <label for="team_name">Enter name: </label>
        <input id="team_name" type="text" name="name_field" value="Default name for team.">
        <input type="submit" value="OK">
    </form>
```
  - The regular HTML form have the  following tags:
    - **Labels**
    - **Inputs fields**
    - **Submit button**
  - The form attributes define the HTTP method used to send the data and the destination of the data on the server (action):
    - **Action**: The URL where data is to be sent for processing when the form is submitted
    - **Method**: The HTTP method used to send the data: POST or GET
      * **POST**: Used to change the data in the database
      * **GET**: Used with forms that do not change the data (e.g. Search), It is recommended for when you want to be able to bookmark or share the URL.
  
## Django form handling process
  - How Django handel the form?
    - The user request the form
    - Then Django handle the request to display the form
    - The user filling the fields and hit the submit button
    - Now, Django handle the request and check if the URL exist to start the process
    - When Django handle the request it fire up the function that related to the URL
    - If the URL not exist, Django will rerender the form with an error message.

## How to create a form using Django
  1. Create a new file in the app folder called form.py
  2. Import forms from the Django library
  3. Create a subclass from the `forms.Form`
  4. Create a variable and assign to it the data type of the field e.g. `renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")`

## Some form fields type 
  - BooleanField
  - CharField
  - ChoiceField
  - TypedChoiceField
  - DateField
  - DateTimeField
  - DecimalField
  - DurationField
  - EmailField
  - FileField
  - FilePathField
  - FloatField
  - ImageField
  - IntegerField
  - GenericIPAddressField
  - MultipleChoiceField
  - TypedMultipleChoiceField
  - NullBooleanField
  - RegexField
  - SlugField
  - TimeField
  - URLField
  - UUIDField
  - ComboField
  - MultiValueField
  - SplitDateTimeField
  - ModelMultipleChoiceField
  - ModelChoiceField.

## Some common arguments to used with fields:
  - **required**: If True, the field may not be left blank or given a None value. Fields are required by default, so you would set required=False to allow blank values in the form.
  - **label**: The label to use when rendering the field in HTML. If a label is not specified, Django will create one from the field name by capitalizing the first letter and replacing underscores with spaces (e.g. Renewal date).
  - **label_suffix**: By default, a colon is displayed after the label (e.g. Renewal date​:). This argument allows you to specify a different suffix containing other character(s).
  - **initial**: The initial value for the field when the form is displayed.
  - **widget**: The display widget to use.
help_text (as seen in the example above  - **):** Additional text that can be displayed in forms to explain how to use the field.
  - **error_messages**: A list of error messages for the field. You can override these with your own messages if needed.
  - **validators**: A list of functions that will be called on the field when it is validated.
  - **localize**: Enables the localization of form data input (see link for more information).
  - **disabled**: The field is displayed but its value cannot be edited if this is True. The default is False.

## Creating a simple form 
  1. From the templates create the HTML form and specify the method type
  2. From the models file, create the table that will holds the user data and specify the inputs fields type.
  3. Register your model in the admin file.
  4. In the view file import the models that you created.
  5. From the view file, go to the function that is responsible of rendering the page.
  6. Pass a request argument to the function.
  7. Declare variables that will carry the user inputs.
  8. To get the user inputs, request the data by using `request.POST.get('field_name_in_html')` or `request.GET.get('field_name_in_html')`
  9. Declare a variable and assign to it an instance of the model, pass the variables that carry user inputs. For example `data = Login(username=username, password=password)`
  10. To save the form into the database run the save method `data.save()`


> **IMPORTANT**: if you use the *POST* method into form, you should validate this form by adding the **`{% csrf_token %}`** tag to the form.This tag will add a layer of security to your form.

---
Resource: [MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
