# THE PAST, PRESENT & FUTURE OF LOCAL STORAGE FOR WEB APPLICATIONS

### Cookies are included with every HTTP request, thereby slowing down your web application by needlessly transmitting the same data over and over

### Cookies are included with every HTTP request, thereby sending data unencrypted over the internet (unless your entire web application is served over SSL)

### Cookies are limited to about 4 KB of data — enough to slow down your application (see above), but not enough to be terribly useful

## INTRODUCING HTML5 STORAGE

### So what is HTML5 Storage? Simply put, it’s a way for web pages to store named key/value pairs locally, within the client web browser.

## USING HTML5 STORAGE

### HTML5 Storage is based on named key/value pairs. You store data based on a named key, then you can retrieve that data with the same key. The named key is a string. The data can be any type supported by JavaScript, including strings, Booleans, integers, or floats. However, the data is actually stored as a string. If you are storing and retrieving anything other than strings, you will need to use functions like parseInt`()` or parseFloat`()` to coerce your retrieved data into the expected JavaScript datatype

## TRACKING CHANGES TO THE HTML5 STORAGE AREA

### If you want to keep track programmatically of when the storage area changes, you can trap the storage event. The storage event is fired on the window object whenever setItem`()`, removeItem`()`, or clear`()` is called and actually changes something. For example, if you set an item to its existing value or call clear`()` when there are no named keys, the storage event will not fire, because nothing actually changed in the storage area.

### The storage event is supported everywhere the localStorage object is supported.

## LIMITATIONS IN CURRENT BROWSERS

### 5 megabytes” is how much storage space each origin gets by default.
