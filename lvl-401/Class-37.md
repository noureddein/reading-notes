#  React 1

## ES6 Overview
### Variables and constant feature comparison
- **let**: Can not be hoisted, it is available into the scope, and can not be re-declared, but can be reassigned.
- **var**: variables with the var keyword can be hoisted, and can be accessed outside of its scope, because it will be hoisted to the top of the code, and it can be re-declared. 
- **const**: variables with the const keyword, they are available into their scope only, and can not be re-declared or reassigned.

### Arrow functions
- Arrow functions are a new way to write functions, see the example below:

```javascript
// The Regular way of functions
function sum(a){
    return a + 5
}

// Arrow functions
let sum = a => return a+ 5
```
- Arrow functions have some constrains you should be aware of them:
  - Arrow functions do not have their own this.
  - Do not have prototypes.
  - Cannot be used for constructors.
  - Should not be used as object methods.

### Template literals
- In ES6 expressions can be embedded in template literal strings, see the example below:
```javascript
// ES5
var str =  'Release date: ' + date

// ES6
let str =  `Release date: ${date}`
```


### Multi-line strings
- In ES6 we can write a multi-line strings using th backtick:
```javascript
// ES5
var str = 'This text ' + 'is on ' + 'multiple lines'

// ES6
const str = `This text
            is on
            multiple lines`
```

### Implicit returns
- If you are using the arrow functions you can omitted the return keyword in case of without a block body.

```javascript
//ES5
function func(a, b, c) {
  return a + b + c
}
//ES6
let func = (a, b, c) => a + b + c // curly brackets must be omitted
```

### Key/property shorthand
- ES6 introduces a shorter notation for assigning properties to variables of the same name.
```javascript
// ES5
var obj = {
  a: a,
  b: b,
}
// ES6
let obj = {
  a,
  b,
}
```


### Method definition shorthand
- The function keyword can be omitted when assigning methods on an object.
```javascript
// ES5
var obj = {
  a: function (c, d) {},
  b: function (e, f) {},
}

// ES6
let obj = {
  a(c, d) {},
  b(e, f) {},
}
obj.a() // call method a
```

### Destructuring (object matching) 
- Use curly brackets to assign properties of an object to their own variable.

```javascript
var obj = {a: 1, b: 2, c: 3}

// ES5
var a = obj.a
var b = obj.b
var c = obj.c
// ES6
let {a, b, c} = obj
```

### Array iteration (looping)
-A more concise syntax has been introduced for iteration through arrays and other iterable objects.

```javascript
var arr = ['a', 'b', 'c']
// ES5
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i])
}

// ES6
for (let i of arr) {
  console.log(i)
}
```

### Default parameters
- Functions can be initialized with default parameters, which will be used only if an argument is not invoked through the function.
```javascript
// ES5
var func = function (a, b) {
  b = b === undefined ? 2 : b
  return a + b
}
// ES6
let func = (a, b = 2) => {
  return a + b
}
func(10) // returns 12
func(10, 5) // returns 15
```

### Spread syntax
- Spread syntax can be used to expand an array.

```javascript
// ES6
let arr1 = [1, 2, 3]
let arr2 = ['a', 'b', 'c']
let arr3 = [...arr1, ...arr2]

console.log(arr3) // [1, 2, 3, "a", "b", "c"]

// ES6
// Spread syntax can be used for function arguments.
let arr1 = [1, 2, 3]
let func = (a, b, c) => a + b + c

console.log(func(...arr1)) // 6
```

### Classes/constructor functions
- ES6 introduces the class syntax on top of the prototype-based constructor function.

```javascript
// ES5
function Func(a, b) {
  this.a = a
  this.b = b
}

Func.prototype.getSum = function () {
  return this.a + this.b
}

var x = new Func(3, 4)

// ES6
class Func {
  constructor(a, b) {
    this.a = a
    this.b = b
  }

  getSum() {
    return this.a + this.b
  }
}

let x = new Func(3, 4)
x.getSum() // returns 7
```


### Inheritance

```javascript
// ES5
function Inheritance(a, b, c) {
  Func.call(this, a, b)

  this.c = c
}

Inheritance.prototype = Object.create(Func.prototype)
Inheritance.prototype.getProduct = function () {
  return this.a * this.b * this.c
}

var y = new Inheritance(3, 4, 5)
```

```javascript
// ES6
class Inheritance extends Func {
  constructor(a, b, c) {
    super(a, b)

    this.c = c
  }

  getProduct() {
    return this.a * this.b * this.c
  }
}

let y = new Inheritance(3, 4, 5)
y.getProduct() // 60
```



### Modules - export/import
- Modules can be created to export and import code between files.

```html
<script src="export.js"></script>
<script type="module" src="import.js"></script>
```
```javascript
// export.js file
let func = (a) => a + a
let obj = {}
let x = 0

export {func, obj, x}
```
```javascript
// import.js file
import {func, obj, x} from './export.js'

console.log(func(3), obj, x)
```

### Promises/Callbacks
- Promises represent the completion of an asynchronous function. They can be used as an alternative to chaining functions.

```javascript
// ES5
function doSecond() {
  console.log('Do second.')
}

function doFirst(callback) {
  setTimeout(function () {
    console.log('Do first.')

    callback()
  }, 500)
}

doFirst(doSecond)
```

```javascript
// ES6
let doSecond = () => {
  console.log('Do second.')
}

let doFirst = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('Do first.')

    resolve()
  }, 500)
})

doFirst.then(doSecond)
```

---

# React

- [x] React - Hello World
- [x] React - JSX
- [x] React - Rendering Elements
- [x] React - Components & Props
- [] React - State & Lifecycle
- [] React - Handling Events

## What is JSX?
```JSX
const element = <h1>Hello, world!</h1>;
```
- This funny tag syntax is neither a string nor HTML, it is called JSX, and it is a syntax extension to JavaScript.
- JSX produces React “elements”.
- Instead of artificially separating technologies by putting markup and logic in separate files, React separates concerns with loosely coupled units called “components” that contain both.

### Embedding Expressions in JSX
- We can add any expression into the JSX, for example: variable, 2 + 2, user.firstName, or formatName(user).

```JSX
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;
```

```JSX
function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};

const element = (
  <h1>
    Hello, {formatName(user)}!
  </h1>
);
```

### JSX is an Expression Too
- After compilation, JSX expressions become regular JavaScript function calls and evaluate to JavaScript objects.
- This means that you can use JSX inside of if statements and for loops, assign it to variables, accept it as arguments, and return it from functions:

```JSX
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}
```
### Specifying Children with JSX
- If a tag is empty, you may close it immediately with />, like XML:

```JSX
const element = <img src={user.avatarUrl} />;
```
```JSX
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

### JSX Prevents Injection Attacks

- It is safe to embed user input in JSX:
```JSX
const title = response.potentiallyMaliciousInput;
// This is safe:
const element = <h1>{title}</h1>;
```
- By default, React DOM escapes any values embedded in JSX before rendering them. Thus it ensures that you can never inject anything that’s not explicitly written in your application. Everything is converted to a string before being rendered. This helps prevent XSS (cross-site-scripting) attacks.


### JSX Represents Objects
- Babel compiles JSX down to React.createElement() calls.
- These two examples are identical:
```JSX
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
```

```JSX
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

## Rendering Elements
- Unlike browser DOM elements, React elements are plain objects, and are cheap to create. React DOM takes care of updating the DOM to match the React elements.

### Rendering an Element into the DOM
- Let’s say there is a <div> somewhere in your HTML file:

```JSX
<div id="root"></div>
```
- We call this a “root” DOM node because everything inside it will be managed by React DOM.

### Updating the Rendered Element
- React elements are **immutable**. Once you create an element, you can’t change its children or attributes. An element is like a single frame in a movie: it represents the UI at a certain point in time.

### React Only Updates What’s Necessary
- React DOM compares the element and its children to the previous one, and only applies the DOM updates necessary to bring the DOM to the desired state.


## Components and Props

### What is Components?
- Components spliting the UI into independent, reusable pieces, and isolated code.
- Conceptually, components are like JavaScript functions. They accept arbitrary inputs (called “props”) and return React elements describing what should appear on the screen. 

### Function and Class Components
- **Function component**: The best way to discribe function component is to write a function.
```JSX
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```
- **Class component**: It is a normal call that inherited from `React.Component` class, and use the `render` method to return elements, look to the example:

```JSX
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```
- The above two components are equivalent from React’s point of view.

### Rendering a Component
- Elements can also represent user-defined components:
```JSX
const element = <Welcome name="Sara" />;
```

- When React sees an element representing a user-defined component, it passes JSX attributes and children to this component as a single object. We call this object “props”.

### Composing Components
- Components can refer to other components in their output. This lets us use the same component abstraction for any level of detail. A button, a form, a dialog, a screen: in React apps, all those are commonly expressed as components.
- For example, we can create an App component that renders Welcome many times:

```JSX
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}
```

### Composing components
- For example, consider this Comment component:
```JSX
    function Comment(props) {
    return (
        <div className="Comment">
        <div className="UserInfo">
            <img className="Avatar"
            src={props.author.avatarUrl}
            alt={props.author.name}
            />
            <div className="UserInfo-name">
            {props.author.name}
            </div>
        </div>
        <div className="Comment-text">
            {props.text}
        </div>
        <div className="Comment-date">
            {formatDate(props.date)}
        </div>
        </div>
    );
    }
```
- This component can be tricky to change because of all the nesting, and it is also hard to reuse individual parts of it. Let’s extract a few components from it.

1.  we will extract Avatar:
```JSX
function Avatar(props) {
  return (
    <img className="Avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}
```
2. Next, we will extract a UserInfo component that renders an Avatar next to the user’s name:

```JSX
function UserInfo(props) {
  return (
    <div className="UserInfo">
      <Avatar user={props.user} />
      <div className="UserInfo-name">
        {props.user.name}
      </div>
    </div>
  );
}
```
- This lets us simplify Comment even further:
```JSX
function Comment(props) {
  return (
    <div className="Comment">
      <UserInfo user={props.author} />
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

### Props are Read-Only
- **Pure vs Impure functions**
  - Pure functions does not change their inputs.
```JSX
function withdraw(account, amount) {
  account.total -= amount;
}
```
  - Impure functions it changes its own input:
```JS
function withdraw(account, amount) {
  account.total -= amount;
}
```
- React is pretty flexible but it has a single strict rule:
- ### **All React components must act like pure functions with respect to their props.**





---

> Notes  
> 1. Since JSX is closer to JavaScript than to HTML, React DOM uses camelCase property naming convention instead of HTML attribute names.
>> For example, class becomes **className** in JSX, and tabindex becomes **tabIndex**.
> 2. React treats components starting with lowercase letters as DOM tags. For example, `<div />` represents an HTML div tag, but `<Welcome />` represents a component and requires Welcome to be in scope.