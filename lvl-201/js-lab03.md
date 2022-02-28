# Chapter 4: Decisions & Loops

## If statements
### The **if** statement evaluates (or checks) a condition. If the condition evaluates to **true**, any statement in the subsequent code block are excuted.

![if-statement](https://github.com/noureddein/reading-notes-201/blob/main/img/if-statement.png?raw=true)

## If...Else statements

### the if..else statement checks a condition.If it resolves to **true** the first code block is excuted.If the condition resolves to **false** the second code block is run insted.

![If-else](https://github.com/noureddein/reading-notes-201/blob/main/img/if-else.png?raw=true)

## Switch Statements
### A switch statment start with a variable called the **switch value**.Each case indicates a possible value for this variable and the code that should run if the variable matches that value.

![Switch-Statements](https://github.com/noureddein/reading-notes-201/blob/main/img/switch-statement.png?raw=true)

## Data type and purpose:

Data type | Purpose
--------- | -------
string | Text
number | Number
Boolean | true or false
null | Empty value
undefined | Variable has been declared but not yet assigned a value

> JavaScript can convert data types behind the scenes to complete an operation. This is known as type coercion. For example, a string 'l' could be converted to a number 1 in the following expression:(' 1' > 0). As a result, the above expression would evaluate to true.

# Summary 
  - Conditional statements allow your code to make decisions about what to do next.
  - Comparison operators (===, ! ==, ==, ! =, <, >, <=, => )are used to compare two operands.
  - Logical operators allow you to combine more than one set of comparison operators. 
  - if ... else statements allow you to run one set of code if a condition is true, and another if it is false
  - switch statements allow you to compare a value against possible outcomes (and also provides a default option if none match). 
  - Data types can be coerced from one type to another. All values evaluate to either truthy or falsy.
  - There are three types of loop: for, while, and do..while. Each repeats a set of statements
