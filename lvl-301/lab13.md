# Sending form data

- The form define how the data will be sent.
- The attributes are designed to let use configure how the request to be sent.
- The action attribute defines where the data gets sent.
- `<form action="https://example.com">` this is absolute URL.
- `<form action="/somewhere_else">` this is a relative URL -- the data will sent to adifferent URL on the same origin.
- `<form>` if we send the data without method, the data will sent to the same page.
- The method attribute defines how data is sent.
- HTTP request consist of two parts:
  -  **Headers**: contain the meatadata
  -  **body**: contain the necessary data for the server to process.
  
## The GET method
  - used by the browser to ask the server to send back a given resource.
  - in this way the **browser** send an empty body BUT if the use this method the data will appended to the URL.
  - The data appended to the URL as a name/value pairs.

## The POST method
  - In this method the body will be fill with data.
  - t's the method the browser uses to talk to the server when asking for a response that takes into account the data provided in the body of the HTTP request: "Hey server, take a look at this data and send me back an appropriate result."
  - When the form submit, the URL will get no data appended to it.

## A special case: sending files

### The enctype attribute

  - If we want to send a file we should take three extra step:
      - Set the method to **POST**
      - Set the value of **enctype** to `multipart/form-data.
      - Include one or more `<input type="file">` controls to allow your use to select the files that will be uploaded.


__*Recourses*__ :  
[Mozilla Developer](https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data)

