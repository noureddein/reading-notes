# React 2

## Conditional Rendering
- We have different ways to render components conditionally:
  - With normal if statement and return the component directly, this method should used with a separate function.
  - Element Variables, assign the component to a variable and render it. 
  - Inline If with Logical && Operator, with this way the result should be True & True to render the component that at the right of the symbol.
  - Inline If-Else with Conditional Operator
  - Preventing Component from Rendering


```jsx
// Consider these two components
function UserGreeting(props) {
  return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>;
}


// The function component will return Greeting or Guest
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

const root = ReactDOM.createRoot(document.getElementById('root')); 
// Try changing to isLoggedIn={true}:
root.render(<Greeting isLoggedIn={false} />);
```
```jsx

// Consider these two components
function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}


class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }

  handleLoginClick() {
    this.setState({isLoggedIn: true});
  }

  handleLogoutClick() {
    this.setState({isLoggedIn: false});
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }

    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root')); 
root.render(<LoginControl />);

```
```jsx
Inline If with Logical && Operator

```

```jsx
render() {
  const isLoggedIn = this.state.isLoggedIn;
  return (
    <div>
      The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
    </div>
  );
}

```


## Lists and Keys


```jsx

class Counter extends Component{
  state={
    count:0,
    tags:[]
 };
  renderTags(){
    if(this.state.tags.length === 0) return <p>There are no tags!</p>;
    return<ul>{this.state.tags.map(tag=><li key={tag}>{tag}</li>)}</ul>;
 }

 render(){
    return(
      <div>
        {this.state.tags.length === 0 && "Please create a new tag!"} Using && operator
        {this.render Tags()} // Using function
      </div>
    )}                            
```


## Lists and Keys
- In JSX we don't the concept of loops, because JSX is not a templating engine it's just a simple syntax that compiled to react elements.

- So who we can render a list of items ?, simply we use arrays methods like map, filter, etc.
- Some Notes to be considered:
  -  when we use map method to render list items, we should be aware of give each child a unique key attribute, because if the state of the react element in virtual DOM changes, React needs quickly to figure out what element is changed and where in the DOM should make the changes to keep the DOM in sync with the virtual DOM.
  - Keys Must Only Be Unique Among Siblings.
  
```JSX
class Counter extends Component{
  state={
    count:0,
    tags:['tag1','tag2','tag3']
 };
  render(){
    return (
      <div>
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <button className="btn btn-secondary btn-sm">Increment</button>
        <ul>
          {this.state.tags.map(tag => <li key={tag}>{tag}</li>)} 
       </ul>
 );
 }
}
```
## Forms
### Controlled Components
- In HTML, form elements such as `<input>,` `<textarea>,` and `<select>` typically maintain their own state and update it based on user input. In React, mutable state is typically kept in the state property of components, and only updated with **setState().**
- We can combine the two by making the React state be the “single source of truth”. Then the React component that renders a form also controls what happens in that form on subsequent user input. An input form element whose value is controlled by React in this way is called a “controlled component”.

```JSX
class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
```
- Because we added the value attribute to the input field and and give it the value from `this.state.value`, the value will be always controlled by React, that's make React state the source of truth.
- Since we using the `onChange` attribute, every keystroke will be update by React state and the displayed value will update as the user types.
- Overall, With a controlled component, the input’s value is always driven by the React state
- This structure can be done on `<input>,` `<textarea>,` and `<select>`.


## Lifting State Up
- When we need to keep two values in sync, we should make their state controlled by the closest ancestor.
- Every input field should be have a single source of truth.


## Composition vs Inheritance
- Composition is the act of combining parts or elements to form a whole.

- Components are the UI building blocks in React applications, like pure functions are the building blocks of function composition.