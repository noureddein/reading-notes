# EJS 

## What is EJS?
- **EJS**: EJS or Embedded Javascript Templating is a templating engine used by Node.js. Template engine helps to create an HTML template with minimal code. Also, it can inject data into HTML template at the client side and produce the final HTML. 

## How to use EJS?
- We need to install the librarie first `npm install ejs`. to use EJS.
- All the files should be write like this to use EJS `<% Name_File.ejs`.


## How to inject values into EJS view?
- To insert data from the server we use these symboles
-  `<%= variablesName %>`
-  `<% logic %>`

> It's used to pass data from the server to HTML file

> We must keep in mind that the data rendered in the server NOT in the client machein.

## What is partials ?
- If we have a code we need to repeat it in all pages for Ex the nav bar, we can write it i a sepated file and write it there, and then include that file in the index.ejs.

## Exampels of tags we can use it:

- `<%` 'Scriptlet' tag, for control-flow, no output
- `<%`_ ‘Whitespace Slurping’ Scriptlet tag, strips all whitespace before it
- `<%=` Outputs the value into the template (HTML escaped)
- `<%-` Outputs the unescaped value into the template
- `<%#` Comment tag, no execution, no output
- `<%%` Outputs a literal '<%'
- `%>` Plain ending tag
- `-%>` Trim-mode ('newline slurp') tag, trims following newline
- _`%>` ‘Whitespace Slurping’ ending tag, removes all whitespace after it

