# Reading and Writing Files in Python
---
# Files
## What is **File**?
  - File is a contiguous set of bytesused to store data, the data is organized in a specific format.

  - Files composed into three main parts:
    - **Header**:metadata about the contents of the file (file name, size, type, and so on)

    - **Data**: contents of the file as written by the creator 
    - **End of file(EOF)**: special character that indicates the end of the file.
  
## File Paths 
  - The file path is a string that represents the location of a file.
  - Major parts of file paths:
    - Folder path
    - File name
    - Extension

```
    Example of a file path:
        /
        │
        ├── path/
        |   │
        │   ├── to/
        │   │   └── cats.gif
        │   │
        │   └── dog_breeds.txt
        |
        └── animals.csv
```

## Line Endings
  - The representation of new line by ISO and ASA is `\r\n`

## Character Encodings
  - Encoding is a translation from byte data to human readable character.
  - Each character have a numerical value.
  - The two most common encoding formats are:
    - **ASCII**: store 128 character
    - **UNICODE**: store 1,114,112 character

# Opening and Closing a File in Python

  - To open a file use the `open()` built-in method, which take a required argument and optional argument. that argument is the path of the file.
  - **Always** we should make sure the file is closed when we finish. To do the use the `close()` method.
```
    Example:
    reader = open('dog_breeds.txt')
    try:
        # Further file processing goes here
    finally:
        reader.close()
```

- Or we can use with statement, which automatically close the file.

```
    Example
    with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here
```

| Character | Meaning |
| --------- | ------- |
| 'r' | Open for reading (default) |
| 'w' | Open for writing, truncating (overwriting) the file first |
| 'rb' or 'wb' | Open in binary mode (read/write using byte data) |

  - There are three different categories of file objects:
    - Text files
    - Buffered binary files
    - Raw binary files

---

# Python Exceptions: An Introduction

---

## Exceptions versus Syntax Errors

  - Syntax errors: occur when the parser detects an incorrect statement.
```
    Example:
    >>> print( 0 / 0 ))
    File "<stdin>", line 1
        print( 0 / 0 ))
                      ^
    SyntaxError: invalid syntax
```
  - **Exception error**: This type of error occurs whenever syntactically correct Python code results in an error.

```
    Example
    >>> print( 0 / 0)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero
```

## Raising an Exception
  - Raise to throw an exception if a condition occurs.

```
    Example
    x = 10
    if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
```

## The AssertionError Exception
  - Assertion is a way to assert that condition should be true to let program continue.

```
    import sys
    assert ('linux' in sys.platform), "This code runs on Linux only."
```

## The try and except Block: Handling Exceptions
  - Try and except are a way to prevent the program from crashing.
  - The try block will read the block statement if the statement throw an error we can told the program what to do, that can be done with the except block.

```
    Example
    try:
        // statement
    except:
        // statement
```

## The else Clause
  - With the else statement we instruct the program to execute a certain block of code if there is no exceptions.

```
    try:
        linux_interaction()
    except AssertionError as error:
        print(error)
    else:
        print('Executing the else clause.')
```

## Cleaning Up After Using finally
  - Finally clause always executed, it does not matter if we encounter an exception or not.

```
    try:
        linux_interaction()
    except AssertionError as error:
        print(error)
    else:
        try:
            with open('file.log') as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print('Cleaning up, irrespective of any exceptions.')
```
--- 

### Summary:
  - **raise** allows you to throw an exception at any time.
  - **assert** enables you to verify if a certain condition is met and throw an exception if it isn’t.
  - In the **try** clause, all statements are executed until an exception is encountered.
  - **except** is used to catch and handle the exception(s) that are encountered in the try clause.
  - **else** lets you code sections that should run only when no exceptions are encountered in the try clause.
  - **finally** enables you to execute sections of code that should always run, with or without any previously encountered exceptions.