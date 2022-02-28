# Javascript Templating Language and Engine— Mustache.js with Node and Express

## Javascript templating is a fast and efficient technique to render client-side view templates with Javascript by using a JSON data source. The template is HTML markup, with added templating tags that will either insert variables or run programming logic.

## The template engine then replaces variables and instances declared in a template file with actual values at runtime, and convert the template into an HTML file sent to the client.

### Mustache.js is used to make a HTML template and fill it from JSON file

## For Ex. `let data = '<p> Name:{{name}}:</p>' + '<p>Phon Number:{{phone}}:</p>'`

## the name and phone above called delimiter or hook

### So,with Mustache.js I can itirate all the items inside the JSON file below and pass it to the templet by `Mustache.render(data,items)`

`[ { "name":"Nour", "phone":"123456" }, { "name":"ahmad", "phone":"123456" } ]`

### to use Mustache we should add the script file to the HTML page `https://cdnjs.cloudflare.com/ajax/libs/mustache.js/4.1.0/mustache.js`

#### Source

[Youtube](https://www.youtube.com/watch?v=mguNnJP5drw) <hr>
[Article](https://1sherlynn.medium.com/javascript-templating-language-and-engine-mustache-js-with-node-and-express-f4c2530e73b2) <hr>
[CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) <hr>
[Flex-box tutorial](https://flexboxfroggy.com/) <hr>
