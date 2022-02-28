# Chapter 2: Text

## Examples of attributs that edit the text?
  * Headings
    * `<h1>` `<h2>` `<h3>` `<h4>` `<h5>` `<h6>`
  * Paragraphs
    * `<p>`
  * Bold & It alic
    * `<b>` for bold
    * `<i>` for italic
  * Superscript & Subscript
    * `<sup>` Superscript the text 
    * `<sub>` Subscript the text
  * Any extra spaces will appear as **one space**
  * Line Breaks & Horizontal Rules
    * `<br/>` To start a new line
    * `<hr/>` To make a Horizontal line

# Summary 
  - 1- HTML elements are used t XX o describe the structure of the page (e.g. headings,subheadings, paragraphs).
  - 2- They also provide semantic information (e.g. where emphasis should be placed, the definition of any acronyms used, when given text is a quotation).
--------------------------------

# Chapter 10: Introducing CSS

## What is CSS:
### CSS stands for **_Cascading Style Sheets_**

>The key to understanding how CSS works is to imagine that there is an invisible box around every HTML element.

>CSS allows you to create rules that control the way that each individual box (and the contents of that box) is presented.

Name Of Element | Block Elements | Inline Elements
--------------- | -------------- | ---------------
Anchor |  | `<a>` | 
Abbreviation |  |`<abbr>`
Bring Attention To element | | `<b>`
Line Break |  | `<br>`
Button |  | `<button>`
Emphasis |  | `<em>`
Image |  | `<img>`
Input |  | `<input>`
Script |  | `<script>`
Address | `<address>` | 
Footer | `<footer>` | 
Horizontal line | `<hr>` | 
Section | `<section>` | 
List | `<li>` | 
Order List | `<ol>` | 
Div | `<div>` | 
Headings (h1 to h6) | `<h1>` to `<h6>`
paragraph | `<p>` |

### CSS works by associating rules with HTML elements. These rules govern how the content of specified elements should be displayed. A CSS rule contains two parts: a **_selector_** and a **_declaration_**.

![Css selector and declaration](https://github.com/noureddein/reading-notes-201/blob/main/img/css-selector-declaration.png?raw=true)

### CSS declarations sit inside curly brackets and each is made up of two parts: a **_property_** and a **_value_**, separated by a colon. You can specify several properties in one declaration, each separated by a semi-colon.

![css-properties-values](https://github.com/noureddein/reading-notes-201/blob/main/img/css-properties-values.png?raw=true)

## How to use an _External_ CSS?
### We can add external css by the _link_ tag `<link href="css/styles.css" type="text/css" rel="stylesheet" />`

### The `<link>` element can be used in an HTML document to tell the browser where to find the CSS file used to style the page. It is an empty element (meaning it does not need a closing tag), and it lives inside the <head> element. It should use three attributes:
   * __href__ : This specifies the path to the CSS file (which is often placed in a folder called css or styles).

   * __type__ : This attribute specifies the type of document being linked to. The value should be text/css.

   * __rel__ : This specifies the relationship between the HTML page and the file it is linked to. The value should be stylesheet when linking to a CSS file.

>An HTML page can use more than one CSS style sheet. To do this it could have a `<link>` element for every CSS file it uses. For example, some authors use one CSS file to control the presentation (such as fonts and colors) and a second to control the layout.

![External-css](https://github.com/noureddein/reading-notes-201/blob/main/img/external-css.png?raw=true)

## How to use an _internal_ css?
### You can also include CSS rules within an HTML page by placing them inside a <style> element, which usually sits inside the `<head>` element of the page.

### The <style> element should use the type attribute to indicate that the styles are specified in CSS. The value should be text/css.

![Internal-css](https://github.com/noureddein/reading-notes-201/blob/main/img/internal-css.png?raw=true)

## CSS Selectors
![css-selectors-table](https://github.com/noureddein/reading-notes-201/blob/main/img/CSS%20selectors.png?raw=true)

## Priority of CSS rules
#### _LAST RULE_ : If the two selectors are identical, the latter of the two will take precedence. Here you can see the second i selector takes precedence over the first.
#### _SPECIFICITY_ : If one selector is more specific than the others, the more specific rule will take precedence over more general ones.
#### _IMPORTANT_ You can add !important after any property value to indicate that it should be considered more important than other rules that apply to the same element.




