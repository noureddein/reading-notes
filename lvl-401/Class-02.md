# Testing and Modules

## Unit test
  - **Unit tests**: Are some pieces of code to exercise the input, output and behavior of the code. 
  - **TDD**: Are stands for Test-Driven Development, it is a strategy of to think.

## Modules
  - If the file invoked directly by its name, Python sets the special `__name__` variable to have a value `__main__`.
  - If the file imported from another module `__name__` will be set to **module_name**.
  - **Module** is a file containing python definitions and statements.
  - The file name is the module name with the suffix .py appended.
  
```
    if '__name__' == '__main__':
        the file will act as a script
    
    if '__name__' == 'filename':
        the file will act as a module
```
---
## Recursion

  - It is a way to make the function call itself, directly or in directly.
  - Every recursion function have a base condition.
  - Without base condition the recursion function will be infinite.
  - Recursive need a **stack** for holding the each recursion.
  - **Direct recursion function**: is the function tha call itself.
  - **Indirect recursion function**: are two functions call each other.
  - Example of recursive functions: 
    - Fibonacci sequence
    - Factorial
    - Towers of Hanoi

---

## Python module and packages
  - Modular programing is breaking a large unwield programming tasks into separate, smaller, more manageable subtasks.
  - Advantages of modularizing code:
    - Simplicity --> to focus on small small portion of problem
    - Maintainability
    - Reusability
    - Scoping

---

## Python List

  * List Methods:
    * list.append(ele): add element to the end of list
    * list.insert(index,ele):  inserts the element at the given index, shifting elements to the right.
    * list.extend(list2) adds the elements in list2 to the end of the list.
    * list.index(elem): searches for the given element from the start of the list and returns its index.
    * ist.remove(elem): searches for the first instance of the given element and removes it.
    * list.sort(): sorts the list in place.
    * list.reverse(): reverses the list in place.
    * list.pop(index): removes and returns the element at the given index.

---
**[Go Back](./README.md)**