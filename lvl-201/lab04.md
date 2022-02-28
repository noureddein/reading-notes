# Chapter 4: Links
## Writing Links
### Links are created using the `<a>` element. Users can click on anything between the opening `<a>` tag and the closing `</a>` tag. You specify which page you want to link to using the href attribute.
![writing-links](https://github.com/noureddein/reading-notes-201/blob/main/img-lab04/writing-links.png?raw=true)
## Linking to Other Pages on the Same Site
### When you are linking to other pages within the same site, you do not need to specify the domain name in the URL. You can use a shorthand known as a relative URL.

## Email Links `mailto:`
### To create a link that starts up the user's email program and addresses an email to a specified email address, you use the `<a>` element. However, this time the value of the href attribute starts with mailto: and is followed by the email address you want the email to be sent to.

![email-links](https://github.com/noureddein/reading-notes-201/blob/main/img-lab04/email-link.png?raw=true)


## Opening Links in a New Window `target`
### If you want a link to open in a new window, you can use the target attribute on the opening `<a>` tag. The value of this attribute should be `_blank`.

![new-window](https://github.com/noureddein/reading-notes-201/blob/main/img-lab04/new-window.png?raw=true)

## Linking to a Specific Part of the Sa me Page
### At the top of a long page you might want to add a list of contents that links to the corresponding sections lower down. Or you might want to add a link from part way down the page back to the top of it to save users from having to scroll back to the top.

### Before you can link to a specific part of a page, you need to identify the points in the page that the link will go to. You do this using the id attribute (which can be used on every HTML element.

### The value of the id attribute should start with a letter or an underscore (not a number or any other character) and, on a single page, no two id attributes should have the same value.
![link-to-the-same-page](https://github.com/noureddein/reading-notes-201/blob/main/img-lab04/link-to-the-same-page.png?raw=true)

# Summary
  - Links are created using the `<a>` element.
  - The `<a>` element uses the href attribute to indicate the page you are linking to.
  - If you are linking to a page within your own site, it is best to use relative links rather than qualified URLs.
  - You can create links to open email programs with an email address in the "to" field.
  - You can use the id attribute to target elements within a page that can be linked to.

----------------------------------

# Chapter 15:Layout
## Key Concepts in Positioning Elements
>CSS treats each HTML element as if it is in its own box. This box will either be a **block-level** box or an **inline box**.

### Block-level boxes start on a new line and act as the main building blocks of any layout, while inline boxes flow between surrounding text. You can control how much space each box takes up by setting the width of the boxes (and sometimes the height, too). To separate boxes, you can use borders, margins, padding, and background colors.

>If one block-level element sits inside another block-level element then the outer box is known as the containing or parent element.

![containing-elements](https://github.com/noureddein/reading-notes-201/blob/main/img-lab04/containing-elements.png?raw=true)

### The orange lines in this diagram represent `<div>` elements. The header (containing the logo and navigation) are in one` <div>` element, the main content of the page is in another, and the footer is in a third. The `<body>` element is the containing element for these three `<div>` elements. The second `<div>` element is the containing element for two paragraphs of Latin text and images (represented by crossed squares).

## Controlling the Position of Elements
### CSS has the following **positioning schemes** that allow you to control the layout of a page: normal flow, relative positioning, and absolute positioning. You specify the positioning scheme using the position property in CSS. You can also float elements using the float property.
   * Normal flow
   * Relative Positioning
   * Ab solute positioning

### To indicate where a box should be positioned, you may also need to use **box offset** properties to tell the browser how far from the top or bottom and left or right it should be placed. (You will meet these when we introduce the positioning schemes on the following pages.)
   * Fixed Positioning
   * Floating Elements

>When you move any element from normal flow, boxes can overlap. The z-index property allows you to control which box appears on top.

## Normal Flow (**Position: static**)
### In normal flow, each block-level element sits on top of the next one. Since this is the default way in which browsers treat HTML elements, you do not need a CSS property to indicate that elements should appear in normal flow, but the syntax would be: **_position: static_**;

## Relative Positioning (**Position: relative**)
### Relative positioning moves an element in relation to where it would have been in normal flow.

### For example, you can move it 10 pixels lower than it would have been in normal flow or 20% to the right.


### You can indicate that an element should be relatively positioned using the position property with a value of relative.

## Absolute Positioning (**Position:absolute**)
### When the position property is given a value of absolute, the box is taken out of normal flow and no longer affects the position of other elements on the page. (They act like it is not there.)

## Fixed Positioning (**Position: fixed**)
### Fixed positioning is a type of absolute positioning that requires the position property to have a value of fixed.

### It positions the element in relation to the browser window. Therefore, when a user scrolls down the page, it stays in the exact same place.

## Overlapping Elements (**z-index**)
### When you use relative, fixed, or absolute positioning, boxes can overlap. If boxes do overlap, the elements that appear later in the HTML code sit on top of those that are earlier in the page.

### If you want to control which element sits on top, you can use the z-index property. Its value is a number, and the higher the number the closer that element is to the front. For example, an element with a z-index of 10 will appear over the top of one with a z-index of 5.

## Floating Elements
### The float property allows you to take an element in normal flow and place it as far to the left or right of the containing element as possible. Anything else that sits inside the containing element will flow around the element that is floated.

## Clearing Floats

### The clear property allows you to say that no element (within the same containing element) should touch the left or right-hand sides of a box. It can take the following values:**Left**, **Right**,**both**,**none**.


## **Screen Sizes**

### Different visitors to your site will have different sized screens that show different amounts of information, so your design needs to be able to work on a range of different sized screens.


## Screen Resolution
### Resolution refers to the number of dots a screen shows per inch. Some devices have a higher resolution than desktop computers and most operating systems allow users to adjust the resolution of their screens.
