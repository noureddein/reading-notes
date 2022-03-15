# List Comprehensions

## What is List Comprehensions?
  - List Comprehensions is an elegant way to create a list.
  - With list comprehension we can write less code.


## What is the syntax of List Comprehensions?
  - `my_new_list = [ expression for item in list ]`
```
    Ex:
        my_nums = [x for x in range(0,10)]
        print(my_nums)

        # Output:
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Does List Comprehensions have an additional features?
  - Yes, we can use if statement with list comprehensions.
```
    Ex:
        fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
        newlist = [x if x != "banana" else "orange" for x in fruits]
        print(newlist)

    #Output:
        ['apple', 'orange', 'cherry', 'kiwi', 'mango']
```
  - We can Multiplying Parts of a List
```
    Ex:
        multiples_of_three = [ x*3 for x in range(10) ]
        print(multiples_of_three)

    # Output:
        [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
``` 

---

# Primer on Decorators

## What is decorators?
  - Decorators are functions takes another functions as arguments.
  - Decorators extend the function behavior.

## What is the components of a function?
  1. Header.
  2. DocString (Optional).
  3. Block statement.
  4. Retaining value
   
```
    EX:
        def add_one(arg):       # Header
            """  A function
                that take an    # DocString
                argument and 
                return it plus
                one 
             """
            result = arg + 1    # Block Statement
            return result       # Retaining value
```

## What is the type of the function?
  - The Function is a first-class object.
  - What first-class mean, that mean the function can be used as an argument.
  - Functions can be stored in a variables.

```
    Ex:
        def my_decorator(func):
            def wrapper():
                print("Something is happening before the function is called.")
                func()
                print("Something is happening after the function is called.")
            return wrapper

        def say_whee():
            print("Whee!")

        say_whee = my_decorator(say_whee)

    #Output:
        Something is happening before the function is called.
        Whee!
        Something is happening after the function is called.
```

## how to create a decorator function?

```
    Ex:
        def f1(func):
            def wrapper(*args, **kwargs):
                print('Started..')
                val = func(*args, **kwargs)
                print('Ended!')
                return val

            return wrapper

        @f1
        def f2():
            print('Printed from F2 Function!!')

        @f1
        def add_values(a, b):
            return a + b

        f2()
        print(add_values(3, 5))
```

  - As you see in the example above, we decorated the **f2** and **add_values** functions with **f1** function.
  - If we invoke function `f2()`, we actually did not invoke it, we pass it to `f1` function as an argument, and the `f1` function return the `wrapper` as function block (not executed yet).
  - The `f2()` statement will not execute the `f2` function, it actually execute the returned wrapper function.


---

## Recourses
  1. [pythonforbeginners](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
  2. [realpython](https://realpython.com/primer-on-python-decorators/)
  3. [w3schools](https://www.w3schools.com/python/python_lists_comprehension.asp)