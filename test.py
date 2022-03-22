from functools import total_ordering


@total_ordering
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

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(self.owner, self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        owner = self.owner + ' & ' + other.owner
        start_amount = self.balance + other.balance
        return Account(owner, start_amount)

    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))


acc = Account('bob', 10)

acc.add_transaction(20)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30)

print('Acc_1 Balance: ', acc.balance)
print('------------------')
print('Total transections: ', len(acc))
for t in acc:
    if t < 0:
        print('Transection: ', t)
        continue
    print('Transection:  ', t)


acc2 = Account('tim', 100)
acc2.add_transaction(20)
acc2.add_transaction(40)
print('\nAcc_2 Balance: ', acc2.balance)
print('------------------')


print(acc2 == acc)

acc3 = acc2 + acc
print(acc())
