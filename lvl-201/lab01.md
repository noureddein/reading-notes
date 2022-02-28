# Chapter 1: Structure 
## What is HTML?
### HTML stands for Hyper Text Markup Language, HTML describes the structure of a Web page, it consists of a series of elements to tell the browser how to display the content.

## How to use HTML?
### To use HTML professionally you need a professional text editor.
#### For Example:
 - 1-	VS code.
 - 2-	Brackets.
 - 3-	Atom.

## What are the components that comprise a standard HTML elements?
 - 1-	Open tag
 - 2-	Closing tag
 - 3-	Content within the tag
 - 4-	Attributes of the tag

### Example of HTML code:
`<html>`
`<body>`
`<h1>`This is the Main Heading`</h1>`
`<p>`This text might be an introduction to the rest of
the page. And if the page is a long one it might
be split up into several sub-headings. `<p>`
`<h2>`This is a Sub-Heading`</h2>`
`<p>`Many long articles have sub-headings so to help
you follow the structure of what is being written.
There may even be sub-sub-headings (or lower-level
headings).`</p>`
`<h2>`Another Sub-Heading`</h2>`
`<p>`Here you can see another sub-heading.`</p>`
`</body>`
`</html>`

* Description of the above code:
[opening and closing tag](https://github.com/noureddein/reading-notes-201/blob/main/img/Opening%20&%20Closing%20tag.png?raw=true)

> Tags act like containers. They tell you something about the information that lies between their opening and closing tags.

* The opening `<html>` tag indicates that anything between it and a closing `</html>` tag is HTML code.
* The `<body>` tag indicates that anything between it and the closing `</body>` tag should be shown inside the main browser window.
* Words between `<h1>` and `</h1>`are a main heading.
* A paragraph of text appears between these `<p>` and `</p>` tags.
* Words between `<h2>` and `</h2>` form a sub-heading.
* The closing `</body>` tag indicates the end of what should appear in the main browser window.
* The closing `</html>` tag indicates that it is the end of the HTML code.

## Attributes: 
### What is attributes?
#### Attributes provide additional information about the contents of an element. They appear on the opening tag of the element and are made up of two parts: a **name** and a **value**, separated by an equal’s sign.

[attributes](https://github.com/noureddein/reading-notes-201/blob/main/img/attributes.png?raw=true)

------------------------------------------------------------

# Chapter 8: Extra Markup

## Versions of HTML:
  * HTML 4 (1997)
  * XHTML (2000)
  * HTML 5 (2000)

## What version we will use and How?
### We will use version 5 of HTML.B ecause there have been several versions of HTML, each web page should begin with a DOCTYPE declaration to tell a browser which version of HTML the page is using (although browsers usually display the page even if it is not included).
[Doctype](https://github.com/noureddein/reading-notes-201/blob/main/img/doctype.png?raw=true)

## How to add comments to code?
### If you want to add a comment to your code that **will not be visible in the user's browser**, you can add the text between these characters: `<!-- comment goes here -->`

[commints](https://github.com/noureddein/reading-notes-201/blob/main/img/commints.png?raw=true)

## How to add properties to elements?
### To add properties to elements you need to use attributes. So, there are two types of attributes:
  - 1-	ID Attribute: which is a unique and used for one **__element only__**.
  - 2-	Class Attribute: which is a global attribute and we can use it with several elements.

## ID Attributes:
### Every HTML element can carry the id attribute. It is used to uniquely identify that element from other elements on the page. Its value should **start with a letter or an underscore** (not a number or any other character). It is important that no two elements on the same page have the same value for their id attributes (otherwise the value is no longer unique).

[id-attribut](https://github.com/noureddein/reading-notes-201/blob/main/img/id-attr.png?raw=true)

## Class Attribute:
### Every HTML element can also carry a class attribute. Sometimes, rather than uniquely identifying one element within a document, you will want a way to identify several elements as being different from the other elements on the page. **__For example__**, you might have some paragraphs of text that contain information that is more important than others and want to distinguish these elements, or you might want to differentiate between links that point to other pages on your own site and links that point to external sites.

[class-attr](https://github.com/noureddein/reading-notes-201/blob/main/img/class-att.png?raw=true)

## Block Elements:
### Some elements will always appear to start on a new line in the browser window. These are known as **block level elements**.

#### Examples of block elements are:
 - `<h1>`
 - `<p>`
 - `<ul>`
 - `<li>`
 - `<div>`

## Inline Elements:
### Some elements will always appear to continue on the same line as their neighboring elements. These are known as **inline elements**.

#### Examples of inline elements are
  - `<a>` 
  - `<b>`
  - `<em>`
  - `<img>`

## Grouping Text & Elements in a Block:
### 1-	`<div>`:
#### The `<div>` element allows you to group a set of elements together in one block-level box. For example, you might create a `<div>` element to contain all of the elements for the header of your site (the logo and the navigation), or you might create a `<div>` element to contain comments from visitors. 
#### In a browser, the contents of the `<div>` element will start on a new line, but other than this it will make no difference to the presentation of the page.

[Div](https://github.com/noureddein/reading-notes-201/blob/main/img/div.png?raw=true)

### 2-	`<span>`: 
#### The `<span>` element acts like an inline equivalent of the `<div>` element. It is used to either:
   - 1. Contain a section of text where there is no other suitable element to differentiate It from its surrounding text.
   - 2. Contain a number of inline elements.

[Span](https://github.com/noureddein/reading-notes-201/blob/main/img/span.png?raw=true)

## 3-	`<iframe>`:
### An iframe is like a little window that has been cut into your page — and in that window you can see another page. The term iframe is an abbreviation of inline frame.
### One common use of iframes (that you may have seen on various websites) is to embed a Google Map into a page. The content of the iframe can be any html page (either located on the same server or anywhere else on the web).

### An iframe is created using the `<iframe>` element. There are a few attributes that you will need to know to use it:

   * **Src:** The src attribute specifies the URL of the page to show in the frame.

   * **Height:** The height attribute specifies the height of the iframe in pixels.

   * **Width:** The width attribute specifies the width of the iframe in pixels.

[iframe](https://github.com/noureddein/reading-notes-201/blob/main/img/ifram.png?raw=true)


## Escape Characters:
[Escape-char](https://github.com/noureddein/reading-notes-201/blob/main/img/syambol.png?raw=true)

----------------------------------------------------------

# Chapter 17:HTML 5 layout

### In older HTML versions an for a long time, web page authors used <div> elements to group together related elements on the page (such as the elements that form a header, an article, footer or sidebar). Authors used class or id attributes to indicate the role of the <div> element in the structure of the page.
[older-browser](https://github.com/noureddein/reading-notes-201/blob/main/img/old-html-versions.png?raw=true)

### The new HTML5 elements indicate the purpose of different parts of a web page and help to describe its structure.

### HTML5 introduces a new set of elements that allow you to divide up the parts of a page. The names of these elements indicate the kind of content you will find in them. They are still subject to change, but that has not stopped many web page authors using them already.

[new-browser](https://github.com/noureddein/reading-notes-201/blob/main/img/new-html-version.png?raw=true)

## Headers & Footers `<header>` `<footer>`:
### The `<header>` and `<footer>` elements can be used for:
  * The main header or footer that appears at the top or bottom of every page on the site.
  * A header or footer for an individual `<article>` or `<section>` within the page.

  [header-footer](https://github.com/noureddein/reading-notes-201/blob/main/img/header-footer.png?raw=true)

## Navigation `<nav>`:
### The `<nav>` element is used to contain the major navigational blocks on the site such as the primary site navigation.

[nav](https://github.com/noureddein/reading-notes-201/blob/main/img/nav.png?raw=true)

## Articles `<article>`:
### The `<article>` element acts as a container for any section of a page that could stand alone and potentially be syndicated.

### The `<article>` elements can even be nested inside each other. For example, a blog post might live inside one `<article>` element and each comment on the article could live inside its own child `<article>` element.

[articale](https://github.com/noureddein/reading-notes-201/blob/main/img/artical.png?raw=true)

## Sections `<section>`

### The `<section>` element groups related content together, and typically each section would have its own heading.
### Alternatively, if you have a page with a long article, the `<section>` element can be used to split the article up into separate sections.
[sections](https://github.com/noureddein/reading-notes-201/blob/main/img/section.png?raw=true)

## How to helping Older Browsers to Understand HTML 5?
### Older browsers that do not know the new HTML5 elements will automatically treat them as inline elements. Therefore, to help older browsers, you should include the line of CSS on the left which states which new elements should be rendered as block-level elements.

### Unfortunately, this workaround does require that anyone using IE8 or earlier versions of IE has JavaScript enabled in their browser. If they do not have JavaScript enabled then they will not be able to see the content of these HTML5 elements.

[older-browser](https://github.com/noureddein/reading-notes-201/blob/main/img/older-browsers.png?raw=true)

--------------------------------- 

# Chapter 18: Process & Design

## Before you creating a web site you must ask yourself these qustions:
  - 1 - Who is the Site For?
  - 2 - Why People Visit YOUR Website?
  - 3 - What Your Visitors are Trying to Achieve?
  - 4 - What Information Your Visitors Need?
  - 5 - How Of ten People Will Visit Your Site?
  

  




















