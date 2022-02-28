# Chapter 15: Layout

## Building Blocks

### CSS treats each HTML element as if it is in its own box. This box will either be a *block-level* box or an *inline box*

### Block-level boxes start on a new line and act as the main building blocks of any layout, while inline boxes flow between surrounding text. You can control how much space each box takes up by setting the width of the boxes (and sometimes the height, too). To separate boxes, you can use borders, margins, padding, and background colors

![block-inlin](./img-lab08/block-inlin.png)

## Containing Elements

### If one block-level element sits inside another block-level element then the outer box is known as the containing or parent element

## Controlling the position of elements

## CSS has the following **positioning schemes** that allow you to control the layout of a page: normal flow, relative positioning, and absolute positioning. You specify the positioning scheme using the position property in CSS. You can also float elements using the float property

* __Normal flow__: Every block-level element appears on a new line, causing each item to appear lower down the page than the previous one. Even if you specify the width of the boxes and there is space for two elements to sit side-byside, they will not appear next to each other. This is the default behavior (unless you tell the browser to do something else).

* __Relative Positioning__:This moves an element from theposition it would be in normalflow, shifting it to the top, right,bottom, or left of where itwould have been placed. Thisdoes not affect the position ofsurrounding elements; they stayin the position they would be inin normal flow.

* __Absolute Positioning__ : This positions the element in relation to its containing element. It is taken out of normal flow, meaning that it does not affect the position of any surrounding elements (as they simply ignore the space it would have taken up). Absolutely positioned elements move as users scroll up and down the page.

## To indicate where a box should be positioned, you may also need to use box offset properties to tell the browser how far from the top or bottom and left or right it should be placed.

__Fixed Positioning__:  This is a form of absolute positioning that positions the element in relation to the browser window, as opposed to the containing element. Elements with fixed positioning do not affect the position of surrounding elements and they do not move when the user scrolls up or down the page.

__Floating elements__: Floating an element allows you to take that element out
 of normal flow and position it to the far left or right of a containing box. The floated element becomes a block-level element around which other content can flow.
