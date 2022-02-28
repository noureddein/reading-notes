# Chapter 5: Images 

>A picture can say a thousand words, and great images help make the difference between an average-looking site and a really engaging one.

## When we choose images it should be:
  - Images should...
  - Be relevant
  - Convey information
  - Convey the right mood
  - Be instantly recognisable
  - Fit the color palette

## When we build a website, all images should be stored in a folser
## To add an image into the page you need to use an `<img src="" alt="" title="">` element
  - **src** :This tells the browser where it can find the image file. This will usually be a relative URL pointing to an image on your own site.
  - **alt**: This provides a text description of the image which describes the image if you cannot see it.
  - **title**: You can also use the title attribute with the `<img>` element to provide additional information about the image. Most browsers will display the content of this attribute in a tootip when the user hovers over the image.

## To control the size of image we use:
  - width and height attributes 
  
## Where to Place Images in Your Code??
  * before a paragraph
  * inside the start of a paragraph
  * in the middle of a paragraph

## Three Rules for Creating Images:
  * Save images in the right format
  * Save images at the right size
  * Use the correct resolution

## Summary 
  - The `<img>` element is used to add images to a web page.
  - You must always specify a src attribute to indicate the source of an image and an alt attribute to describe the content of an image.
  - You should save images at the size you will be using them on the web page and in the appropriate format.
  - Photographs are best saved as JPEGs; illustrations or logos that use flat colors are better saved as GIFs.
  
------------------------------------------

# Chapter 11: Color

## How to specify colors?
### We can specify colors in three ways
  - rgb values
  - hex codes
  - color names

> Every color on a computer screen is created by mixing amounts of red, green, and blue. To find the color you want, you can use a color picker

# Chapter 11: Colors
### To specify a color in CSS there are several ways :
  - 1-	RGB values
     * Ex. rgb(102,205,170)
  - 2-	HEX codes
     * Ex. #66cdaa
  - 3-	Color names
     * Ex. MediumAquaMarine
  - 4-	HSLA (Hue, Saturation, Luminosity, Alpha) 
     * Ex. hsla(360, 100%, 100%, 0.5)

## Opacity 
### CSS3 introduces the opacity property which allows you to specify the opacity of an element and any of its child elements. The value is a number between **0.0** and **1.0** (so a value of 0.5 is 50% opacity and 0.15 is 15% opacity).

### The CSS3 **RGBa** property allows you to specify a color, just like you would with an RGB value, but adds **a** fourth value to indicate _opacity_. This value is known as an **_alpha-** value and is a number between 0.0 and 1.0 (so a value of 0.5 is 50% opacity and 0.15 is 15% opacity). The rgba value will only affect the element on which it is applied (not child elements).

### Margin, Padding, and Border
![Margin and Padding](https://github.com/noureddein/reading-notes/blob/main/imgs/Paddin%20and%20margin.png?raw=true)

### How to add styling to elements
![Add Properties](https://github.com/noureddein/reading-notes/blob/main/imgs/properteis%20and%20valuse.png?raw=true)

## Summary 
  - 1-Color not only brings your site to life, but also helps convey the mood and evokes reactions.
  - 2-There are three ways to specify colors in CSS: RGB values, hex codes, and color names.
  - 3-Color pickers can help you find the color you want.
  - 4-It is important to ensure that there is enough contrast between any text and the background color (otherwise people will not be able to read your content).
  - 5-CSS3 has introduced an extra value for RGB colors to indicate opacity. It is known as RGBA.
  - 6-CSS3 also allows you to specify colors as HSL values, with an optional opacity value. It is known as HSLA.

---------------------------------------

# Chapter 12: Text

## Typeface Terminology
![typeface-termi](https://github.com/noureddein/reading-notes-201/blob/main/img-lab05/typeface-termo.png?raw=true)
![typeface-termi2](https://github.com/noureddein/reading-notes-201/blob/main/img-lab05/typeface-termo2.png?raw=true)

## Choosing a Typeface for your Website
### When choosing a typeface, it is important to understand that a browser will usually only display it if it's installed on that user's computer.

![fonts](https://github.com/noureddein/reading-notes-201/blob/main/img-lab05/fots.png?raw=true)

>You can specify a list of fonts separated by commas so that, if the user does not have your first choice of typeface installed,the browser can try to use an alternative font from the list.

## Size of Type (font-size)

### The font-size property enables you to specify a size for the font. There are several ways to specify the size of a font. The most common are:
   * **pixels**
   * **percentages**
   * **ems**

## Type Scales
### You may have noticed that programs such as Word, Photoshop and InDesign offer the same sizes of text.

#### This is because they are set according to a scale or ratio that was developed by European typographers in the sixteenth century.

## Units of Type Size
![unit-of-type size](https://github.com/noureddein/reading-notes-201/blob/main/img-lab05/unit%20of%20typr%20size.png?raw=true)

>Setting font size in pixels is the best way to ensure that the type appears at the size you intended.

>The default size of text in a web browser is 16 pixels.

## More Font Choice (@font-face)
### @font-face allows you to use a font, even if it is not installed on the computer of the person browsing, by allowing you to specify a path to a copy of the font, which will be downloaded if it is not on the user's machine.
![font@face](https://github.com/noureddein/reading-notes-201/blob/main/img-lab05/font@face.png?raw=true)

  - **font-family**:This specifies the name of the font. This name can then be used as a value of the font-family property in the rest of the style sheet (as shown in the rule for the `<h1>` and `<h2>` elements).

  - **src**:  This specifies the path to the font. In order for this technique to work in all browsers, you will probably need to specify paths to a few different versions of the font, as shown on the next page.

  - **format**:  This specifies the format that the font is supplied in.

