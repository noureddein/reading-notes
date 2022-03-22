# Dunder Methods

## What Are Dunder Methods?
  - **Dunder Methods** are a special predefined methods used to enrich the classes.
  - The **Dunder Methods** start and end with double under scores `__init__`, `__call__`.
  - **Dunder** is a short term of _double under_.

## Dunder methods examples

  - Object Initialization: `__init__`
    - `__init__` is used to construct the object from the class.
    - The constructor takes care of setting up the object
```
    class Account:
        """A simple account class"""

        def __init__(self, owner, amount=0):
            """
            This is the constructor that lets us create
            objects from this class
            """
            self.owner = owner
            self.amount = amount
            self._transactions = []
```

  - Object Representation: `__str__`, `__repr__`
    - `__repr__`: The “official” string representation of an object. The goal of `__repr__` is to make the class unambiguous.
    - `__str__`: The “informal” or nicely printable string representation of an object. This is for the enduser.

```
    class Account:
    # ... (see above)

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)
```

  - Iteration: `__len__`, `__getitem__`, `__reversed__`
    - `__len__`: To use the regular **len** function with the objects we need to defined that in the class.
    - `__getitem__`: Used to make the instance iterable.
    - `__reversed__`: To use the regular **reverse** function with the objects we need to defined that in the class.


```
    class Account:
        # ... (see above)

        def __len__(self):
            return len(self._transactions)

        def __getitem__(self, position):
            return self._transactions[position]

        def __reversed__(self):
        return self[::-1]
```

  - Operator Overloading for Comparing Accounts: `__eq__`, `__lt__`
    - We can use operators with normal variables, but we can not use them with instances, except if we defined it explicitly.
    - To use the operation methods we need a module called **functools**, and add a decorator above the class `@total_ordering`.
```
    from functools import total_ordering

    @total_ordering
    class Account:
        # ... (see above)

        def __eq__(self, other):
            return self.balance == other.balance

        def __lt__(self, other):
            return self.balance < other.balance
```

  - Operator Overloading for Merging Accounts: `__add__`
    - In normal way, we can use `+` operator to sum two numbers, or even to concatenate two strings. But with objects we need to defined that explicitly.

```
    def __add__(self, other):
        owner = self.owner + ' & ' + other.owner
        start_amount = self.balance + other.balance
        return Account(owner, start_amount)
```

  - Callable Python Objects: `__call__`
    - With the call method we can make the object callable, and print a nicely report.

```
    class Account:
    # ... (see above)

    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))
```

