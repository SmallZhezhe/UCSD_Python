"""a Simple BankAccount class"""
from functools import total_ordering


@total_ordering
class BankAccount:
    """ Simple BankAccount class """

    def __init__(self, balance=0):
        """Initialize account with balance"""
        self.balance = balance
        self.transactions = [("OPEN", balance, balance)]
        print("Account opened.")
        self.print_balance()

    def deposit(self, amount):
        """Deposit amount to this instance"""
        self.balance += amount
        self.transactions.append(("DEPOSIT", amount, self.balance))
        print("${} deposited.".format(amount))
        self.print_balance()

    def withdraw(self, amount):
        """Withdraw amount from this instance"""
        self.balance -= amount
        self.transactions.append(("WITHDRAWAL", -amount, self.balance))
        print("${} withdrawn.".format(amount))
        self.print_balance()

    def print_balance(self):
        """Print the balance of this instance"""
        print("Account balance is ${}.".format(self.balance))

    def transfer(self, other_account, amount):
        """Transfer the amount from this instance to other_account"""
        self.withdraw(amount)
        other_account.deposit(amount)

    def __str__(self):
        """User-friendly printing"""
        return "Account with balance of ${}".format(self.balance)

    def __repr__(self):
        """Developer-friendly printing"""
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



class MinimumBalanceAccount(NamedAccount):

    """Bank account which does not allow balance to drop below zero."""

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Balance cannot be less than $0!")
        return super().withdraw(amount)
