# Chapter 3:WHAT IS AN OBJECT?
## Objects group together a set of variables and functions to create a model of a something you would recognize from the real world. In an object, variables and functions take on new names.

### IN AN OBJECT: VARIABLES BECOME KNOWN AS PROPERTIES

## Creating an object:
### Literal notation is the easiest and most popular way to create objects.

![literal-notation-method](https://github.com/noureddein/reading-notes-201/blob/main/img-lab06/literal-notation-method.png?raw=true)

## Accessing an Object and Dot notation
### You can access the properties or methods of an object using dot notation.and you can also access properties using square brackets.
![accessing-an-object-and-dot-notation.png](https://github.com/noureddein/reading-notes-201/blob/main/img-lab06/accessing-an-object-and-dot-notation.png?raw=true)

--------------------------------

# Chapter 5:Document Object Model

## The Document Object Model (DOM) specifies how browsers should create a model of an HTML page and how JavaScript can access and update the contents of a web page while it is in the browser window.

### The DOM is neither part of HTML, nor part of JavaScript; it is a separate set of rules.It is implemented by all major browser makers, and covers two primary areas:
   * MAKING A MODEL OF THE HTML PAGE
   * ACCESSING AND CHANGING THE HTML PAGE

### As a browser loads a web page, it creates a model of that page. The model is called a DOM tree, and it is stored in the browsers' memory. It consists of four main types of nodes.

![DOM-tree](https://github.com/noureddein/reading-notes-201/blob/main/img-lab06/dom0tree.png?raw=true)

## WORKING WITH THE DOM TREE:
### Accessing and updating the DOM tree involves two steps:
  - 1 Locate the node that represents the element you want to work with.
  - 2 Use its text content, child elements, and attributes.

### STEP 1: ACCESS THE ELEMENTS:
   - SELECT AN INDIVIDUAL ELEMENT NODE
   - SELECT MULTIPLE ELEMENTS (NODELISTS)
   - TRAVERSING BETWEEN ELEMENT NODES

> The terms **elements** and **element nodes** are used interchangeably
but when people say the DOM is working with an element,
it is actually working with a node that *represents* that element.

### STEP 2: WORK WITH THOSE ELEMENTS:
   - ACCESS/ UPDATE TEXT NODES
   - WORK WITH HTML CONTENT
   - ACCESS OR UPDATE ATTRIBUTE VALUES

## Caching DOM Queries
### Methods that find elements in the DOM tree are called DOM queries.When you need to work with an element more than once, you should use a variable to store the result of this query.

![Caching DOM Queries]()

## METHODS THAT SELECT INDIVIDUAL ELEMENTS
### get El ementByld () and querySe l ector () can both search an entire document and return individual elements. Both use a similar syntax.
![select-indivual-element]()

## SELECTING- AN ELEMENT FROM A NODELIST
### There are two ways to select an element from a Nodelist: 
   - The item() method
   -  and array syntax.
### Both require the index number of the element you want.


