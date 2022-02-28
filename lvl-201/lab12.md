## EASILY CREATE STUNNING ANIMATED CHARTS WITH CHART.JS (Articl)

## Charts are far better for displaying data visually than tables and have the added benefit that no one is ever going to press-gang them into use as a layout tool. They’re easier to look at and convey data quickly, but they’re not always easy to create.

## Setting up

### The first thing we need to do is download Chart.js. Copy the Chart.min.js out of the unzipped folder and into the directory you’ll be working in. Then create a new html page and import the script:

`<!DOCTYPE html>`
`<html lang="en">`
`` <head>` <meta charset="utf-8" />` ` <title>Chart.js demo</title>` ` <script src='Chart.min.js'></script>` ` </head>` ` <body>` ` </body>` `</html>`

## Drawing a line chart

### To draw a line chart, the first thing we need to do is create a canvas element in our HTML in which Chart.js can draw our chart. So add this to the body of our HTML page:

`<canvas id="buyers" width="600" height="400"></canvas>`

## Next, we need to write a script that will retrieve the context of the canvas, so add this to the foot of your body element:

`<script>`
` var buyers = document.getElementById('buyers').getContext('2d');`
` new Chart(buyers).Line(buyerData);`
`</script>`

## Inside the same script tags we need to create our data:

`var buyerData = {`
`labels : ["January","February","March","April","May","June"],`
`datasets : [`
`{`
`fillColor : "rgba(172,194,132,0.4)",`
`strokeColor : "#ACC26D",`
`pointColor : "#fff",`
`pointStrokeColor : "#9DB86D",`
`data : [203,156,99,251,305,247]`
`}`
`]`
`}`

**Recourse:**
[EASILY CREATE STUNNING ANIMATED CHARTS WITH CHART.JS (](https://www.webdesignerdepot.com/2013/11/easily-create-stunning-animated-charts-with-chart-js/)

---

# Basic usage of canvas

## At first sight a `<canvas>` looks like the `<img>` element, with the only clear difference being that it doesn't have the src and alt attributes. Indeed, the `<canvas>` element has only two attributes, width and height. These are both optional and can also be set using DOM properties. When no width and height attributes are specified, the canvas will initially be 300 pixels wide and 150 pixels high. The element can be sized arbitrarily by CSS, but during rendering the image is scaled to fit its layout size: if the CSS sizing doesn't respect the ratio of the initial canvas, it will appear distorted.

> The id attribute isn't specific to the `<canvas>` element but is one of the global HTML attributes

## Fallback content

### Providing fallback content is very straightforward: just insert the alternate content inside the `<canvas>` element. Browsers that don't support `<canvas>` will ignore the container and render the fallback content inside it. Browsers that do support `<canvas>` will ignore the content inside the container, and just render the canvas normally.
