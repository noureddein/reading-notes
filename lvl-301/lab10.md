# Call stack

## What is call stak?

- **Call Stack** is a mechanism for an interpreter to invoke the functions, its like container for when functions invoked and all of them depending on each other.

## HoW call stak works?

- Lets say we have these functions
  > `function greeting(){ sayHi();}`  
  > `function sayHi() { return "Hi!"; }`  
  > `greeting();`
- When the interpreter reach `greeting();` it will added to the call stak and will executed then it will execute the `sayHai();` function and add it to the call stak. when the interpreter done executing it will return the value to the greeting function and delete it from thr call stack.
- When the value returned to greeting function the call stak delete the function.

- **Call stack** is a _Temporarily store_.
  ![Call-Stack-Store](https://cdn-media-1.freecodecamp.org/images/QgR2uIk7tW0YNz0Xm8g0jAPeRFI0e4sCejsv)

- The code execution in _JavaScript_ are synchronous.

## What is stack overflow?

- Thats happened when execute the function itself inside it, so there are no exit point

---

# JavaScript error messages && debugging

![Photo](https://miro.medium.com/max/500/1*LHpmsxV3f2znpxhuAFuIqA.png)

## Types of error messages

- 1- **Reference errors**: when we try to use a variable that is not yet declared we get this type of errors.
  - Ex `console.log(foo) // Uncaught ReferenceError: foo is not defined`
- 2- **Syntax errors**: This occurs when we have something that cannot be parsed in terms of syntax.
  - Ex: `JSON.parse( {'foo': 'bar'} ) // Uncaught SyntaxError: Unexpected token o in JSON at position 1`.
- 2- **Range errors**: This type when manipulate an object with some kind of length and give it an invalid length
  - Ex: `var foo= [] foo.length = foo.length -1 // Uncaught RangeError: Invalid array length`.
- 3- **Type errors**: This types of errors show up when the types we are trying to use or access are incompatible.
  - Ex:`var foo = {} foo.bar // undefined foo.bar.baz // Uncaught TypeError: Cannot read property 'baz' of undefined`.

---

# Debugging

- Debugging is a way to find out whats happened with our code, It's like when we output something in `console.log()` to see if it have errors or not.

---

# Handling errors

- Handling errors its way to find out what make the error, and we can use **try ... catch** to handle the error.
