# Chapter 3:Lists

## Types of List:
  - 1- Ordered lists
  - 2- Unordered Lists
  - 3- Definition lists

### Ordered list:
The ordered list is created with the `<ol>` element. Each item in the list is placed between an opening `<li>` tag and a closing `</li>` tag (The li stands for list item.)

![or-li](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/or-li.png?raw=true)

### Unordered Lists:
The unordered list is created with the `<ul>` element.Each item in the list is placed between an opening `<li>` tag and a closing `</li>` tag (The li stands for list item.)

![ul-li](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/ul-li.png?raw=true)

### Definition Lists:
**`<dl>`** : The definition list is created with the `<dl>` element and usually consists of a series of terms and their definitions.Inside the `<dl>` element you will usually see pairs of `<dt>` and `<dd>` elements.

**`<dt>`**:This is used to contain the term being defined (the definition term).

**`<dd>`**: This is used to contain the definition
![dl-li](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/dl-li.png?raw=true)

### Nested Lists:
You can put a second list inside an `<li>` element to create a sublist or nested list.Browsers display nested lists indented further than the parent list. In nested unordered lists, the browser will usually change the style of the bullet point too.

![nested-li](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/nested-li.png?raw=true)
-------------------------------
# Chapter 13:Boxes

## Box Dimensions (width & height)
### We can change the dimension of box by adding the attribute to css and change its width and height.

![width-height](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/width-hieght.png?raw=true)

## Limiting Width (min-width, max-width)
### Some page designs expand and shrink to fit the size of the user's screen. In such designs, the min-width property specifies the smallest size a box can be displayed at when the browser window is narrow, and the max-width property indicates the maximum width a box can stretch to when the browser window is wide.

![min-max-width](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/min-max-width.png?raw=true)

## Limiting height (min-height, max-height)
### In the same way that you might want to limit the width of a box on a page, you may also want to limit the height of it. This is achieved using the min-height and max-height properties. The example on this page demonstrates these properties in action. It also shows you what happens when the content of the box takes up more space than the size specified for the box.

## Overflowing Content:
### The overflow property tells the browser what to do if the content contained within a box is larger than the box itself. It can have one of two values:
   * Hidden: This property simply hides any extra content that does not fit in the box.
   * Scroll: This property adds a scrollbar to the box so that users can scroll to see the missing content. 

## Every box has three available properties that can be adjusted to control its appearance:
   - Border: Every box has a border (even if it is not visible or is specified to be 0 pixels wide). The border separates the edge of one box from another.
   - Margin: Margins sit outside the edge of the border. You can set the width of a margin to create a gap between the borders of two adjacent boxes.
   - Padding: Padding is the space between the border of a box and any content contained within it. Adding padding can increase the readability of its contents.

## Border Width:
### The border-width property is used to control the width of a border. The value of this property can either be given in pixels or using one of the following values:**thin, medium, thick**

### You can control the individual size of borders using four separate properties:
   - border-top-width
   - border-right-width
   - border-bottom-width
   - border-left-width

## Border Style:
### You can control the style of a border using the border-style property. This property can take the following values:
  - solid
  - dotted
  - dashed
  - double
  - groove
  - ridge
  - inset
  - outset
  - hidden / none
  
![border-style](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/border-style.png?raw=true)

## Border color: 
### You can specify the color of a border using either RGB values, hex codes or CSS color names (as you saw on pages 251-252).
### It is possible to individually control the colors of the borders on different sides of a box using:
   - border-top-color
   - border-right-color
   - border-bottom-color
   - border-left-color

![border-color](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/border-color.png?raw=true)

## Padding:
### The padding property allows you to specify how much space should appear between the content of an element and its border.And you can control Padding by:
  - padding-top
  - padding-right
  - padding-bottom
  - padding-left

## Margin:
### The margin property controls the gap between boxes. Its value is commonly given in pixels, although you may also use percentages or ems.And you can control margin by:
  - margin-top
  - margin-right
  - margin-bottom
  - margin-left

## Centering Content:
### If you want to center a box on the page (or center it inside the element that it sits in), you an set the left-margin and right-margin to auto. In order to center a box on the page, you need to set a width for the box (otherwise it will take up the full width of the page).
![Centering Content](https://github.com/noureddein/reading-notes-201/blob/main/img-lab03/centerin-content.png?raw=true)

<hr>

# Summary:
 - 1- CSS treats each HTML element as if it has its own box.
 - 2- You can use CSS to control the dimensions of a box.
 - 3- You can also control the borders, margin and padding for each box with CSS.
 - 4- It is possible to hide elements using the display and visibility properties.
 - 5- Block-level boxes can be made into inline boxes, and inline boxes made into block-level boxes.
 - 6- Legibility can be improved by controlling the width of boxes containing text and the leading.
 - 7- CSS3 has introduced the ability to create image borders and rounded borders.




