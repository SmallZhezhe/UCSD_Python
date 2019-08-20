"""Utilities and objects for managing bank accounts."""
from functools import total_ordering


@total_ordering
class BankAccount:
    """Bank account including an account balance."""

    def __init__(self, balance=0):
        """Open an account."""
        self.balance = balance
        self.transactions = [("OPEN", balance, balance)]
        print("Account opened.")
        self.print_balance()

    def deposit(self, amount):
        """Increase the account balance."""
        self.balance += amount
        self.transactions.append(("DEPOSIT", amount, self.balance))
        print("${} deposited.".format(amount))
        self.print_balance()

    def withdraw(self, amount):
        """Decrease the account balance."""
        self.balance -= amount
        self.transactions.append(("WITHDRAWAL", -amount, self.balance))
        print("${} withdrawn.".format(amount))
        self.print_balance()

    def print_balance(self):
        """Print the current account balance."""
        print("Account balance is ${}.".format(self.balance))

    def transfer(self, other_account, amount):
        """Move money from our account to the given account."""
        self.withdraw(amount)
        other_account.deposit(amount)

    def __str__(self):
        """Return a human-readable explanation of account."""
        return "Account with balance of ${}".format(self.balance)

    def __repr__(self):
        """Return a developer-readable representation of our account."""
        return "BankAccount(balance={})".format(self.balance)

    def __bool__(self):
        return self.balance > 0

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


class NamedAccount(BankAccount):

    """Bank account with an account name."""

    def __init__(self, *args, **kwargs):
        """Open a named bank account."""
        self.name = kwargs.pop('name', None)
        super().__init__(*args, **kwargs)

    def print_balance(self):
        """Print the account name and current account balance."""
        print('Account "{}" balance is ${}'.format(self.name, self.balance))

    def __str__(self):
        """Return account name and balance."""
        return 'Account "{name}" with balance of ${balance:.2f}'.format(
            name=self.name,
            balance=self.balance,
        )

    def __repr__(self):
        """Return developer-readable representation of our named account."""
        return 'NamedAccount(balance={balance:.2f}, name={name})'.format(
            balance=self.balance,
            name=repr(self.name),
        )


class MinimumBalanceAccount(BankAccount):

    """Bank account which does not allow balance to drop below zero."""

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Balance cannot be less than $0!")
        return super().withdraw(amount)

"""For REPL
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
