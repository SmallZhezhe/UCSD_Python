class NamedAccount(BankAccount):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', None)
        super().__init__(*args, **kwargs)
    def print_balance(self):
        print('Account "{}" balance is ${}'.format(self.name,
            self.balance))
    def __str__(self):
        return 'Account "{}" with balance of ${}'.format(self.name,
            self.balance)
    def __repr__(self):
        return 'NamedAccount(name={}, balance={})'.format(self.name,
            self.balance)



from bank_account import NamedAccount
bob_account = NamedAccount(name="Bob", balance=350)
bob_account.name
bob_account

nameless_account = NamedAccount()
nameless_account.name
nameless_account.name is None
nameless_account

bob_account.deposit(825)
bob_account.withdraw(150)
bob_account.deposit(3.55)
bob_account.deposit(12.25)



"""
from bank_account import BankAccount
my_account = BankAccount()
my_account.deposit(1000)
sue_account = BankAccount()
sue_account.deposit(350)
my_account.transfer(sue_account, 100)
"""


class BankAccount:
    """ Simple BankAccount class """

    def __init__(self, balance=0):
        """Initialize account with balance"""
        self.balance = balance
        print("Account opened.")
        self.print_balance()


class NamedAccount(BankAccount):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', None)
        super().__init__(*args, **kwargs)
    def print_balance(self):
        print('Account "{}" balance is ${}'.format(self.name,
            self.balance))
    def __str__(self):
        return 'Account "{}" with balance of ${}'.format(self.name,
            self.balance)
    def __repr__(self):
        return 'NamedAccount(balance={}, name={})'.format(self.balance,
            self.name)
