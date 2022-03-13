# Globals
  - Modules: The global scope
  - The global statement
  - globals()


## The Global Scope
   - Pthon turns program main script into a module called **__main__**.
   - Any name defined at the top level of python program will considered global to the module.
   - The global names can not be changed in a local scope.

```
    var = 100
    def func():
        var = 200
        return var

    print(func())
    print(var)

    # output:
        200
        100
```
  - The **var** at the top called **_global_** 
  - The **var** at in the _func()_ called **_local_** 
  - The **var** in side the function will not affect the **var** at the top level, because Python will create a local variable called **var**.
  - To change the global variable **var** we need to explicitly told Python to use the global variable and change it's value.
  - Each function has its own local scope.


## The Global Statement
  - The **global** keyword followed by one or more names separated by commas will tell Python to used the global names.

```
    counter = 0
    def update_counter():
        counter = counter + 1 
        return counter
    print(update_counter())

    # Output:
        UnboundLocalError: local variable 'counter' referenced before assignment
```
  - The piece of code above will end up with error, because:
    - We cannot access the global variable.
    - We update a variable before declare it.


  - To solve the error occurred above we do the following:

```
    counter = 0
        def update_counter():
            global counter
            counter = counter + 1 
            return counter
        print(update_counter())

        # Output:
            1
```
  
  - We can make a local name global by defining it as a global inside the block of a function.

```
    def create_global():
        global var
        var = 50
    
    print(var)

    # Output:
        50
```

## globals() Function
  - globals() function stored all the names of the current module.
  - globals() is a built-in function and return a dictionary containing all the names

# The nonlocal Statement
  - **nonlocal** keyword used to modify a name that in a local of function.

```
    def func():
        var = 100
        def nested():
            nonlocal var
            var += 100
        nested()
        print(var)

    func()

    # Output:
        200
```

 