# Regex

### Regular expressions (regex or regexp) are extremely useful in extracting information from any text by searching for one or more matches of a specific search pattern (i.e. a specific sequence of ASCII or unicode characters).

### Examples and explanations.

#### Anchors — ^ and $

| Sign        | Explanations                                      |
| ----------- | ------------------------------------------------- |
| `^The`      | matches any string that starts with The           |
| `end$`      | matches a string that ends with end               |
| `^The end$` | exact string match (starts and ends with The end) |
| `roar`      | matches any string that has the text roar in it   |

#### Quantifiers — \* + ? and {}

| Sign         | Explanations                                                                   |
| ------------ | ------------------------------------------------------------------------------ |
| `abc*`       | matches a string that has ab followed by zero or more c                        |
| `abc+`       | matches a string that has ab followed by one or more c                         |
| `abc?`       | matches a string that has ab followed by zero or one c                         |
| `abc{2}`     | matches a string that has ab followed by 2 c                                   |
| `abc{2,}`    | matches a string that has ab followed by 2 or more c                           |
| `abc{2,5}`   | matches a string that has ab followed by 2 up to 5 c                           |
| `a(bc)*`     | matches a string that has a followed by zero or more copies of the sequence bc |
| `a(bc){2,5}` | matches a string that has a followed by 2 up to 5 copies of the sequence bc    |

---

# CSS Grid

## In CSS grid we can not only arrange elements in a row or a column, but in multiple rows and columns. Finally two dimensional layouts are becoming simpler!

## Grid gives us control over how wide or narrow each of the ‘grid cells’ get.

`grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));`

### The `repeat()` function takes two arguments, the first will define the number of column tracks and the second, what width the tracks should be.

### In this case, for the first argument, I’ve used `auto-fill` which will create a grid with as many tracks as will fit into the container. The second argument, which defines the width of the tracks, I’ve set to `minmax(250px, 1fr)`. The minmax function will create track widths that can be a minimum of 250px wide and a maximum of 1fr. An fr is a ‘fraction unit’, a unit of measurement to define a fraction of the available space of the container. The width of the elements in the row will increase from 250px until the point where another element could potentially fit beside the first. Try changing the width of your browser while looking at the example to see this in action.

#### Source

[Regex Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285) <hr>
[CSS Tricks](https://css-tricks.com/snippets/css/complete-guide-grid/#prop-display) <hr>
[Article](https://medium.com/samsung-internet-dev/common-responsive-layouts-with-css-grid-and-some-without-245a862f48df)
