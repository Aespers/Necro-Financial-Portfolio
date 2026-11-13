from abc import ABC, abstractmethod
from math import isfinite

from finance_error import FinanceError
from invalid_amount_error import InvalidAmountError
from transaction import Transaction
from withdrawal_error import WithdrawalError


class Account(ABC):
    """Store an account balance and its processed transactions."""

    def __init__(
        self, account_num: int, account_type: str, balance: int | float,
        client_num: int
    ) -> None:
        if type(account_num) is not int or account_num <= 0:
            raise ValueError("Account number must be a positive integer.")
        if not isinstance(account_type, str) or not account_type.strip():
            raise ValueError("Account type must not be empty.")
        if not self.valid_amount(balance, allow_zero=True):
            raise ValueError("Balance must be a non-negative number.")
        if type(client_num) is not int or client_num <= 0:
            raise ValueError("Client number must be a positive integer.")
        self.__account_num = account_num
        self.__account_type = account_type
        self.__balance = balance
        self.__client_num = client_num
        self.__transaction_collection: list[Transaction] = []

    def get_account_num(self) -> int:
        return self.__account_num

    def get_account_type(self) -> str:
        return self.__account_type

    def get_balance(self) -> int | float:
        return self.__balance

    def get_client_num(self) -> int:
        return self.__client_num

    def get_transaction_collection(self) -> list[Transaction]:
        """Return a copy of the transaction history in order."""
        return self.__transaction_collection.copy()

    AccountNum = property(get_account_num)
    AccountType = property(get_account_type)
    Balance = property(get_balance)
    ClientNum = property(get_client_num)
    TransactionCollection = property(get_transaction_collection)

    def __str__(self) -> str:
        return (f"{self.AccountNum}, {self.AccountType}, "
                f"{self.Balance}, {self.ClientNum}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(account_num={self.AccountNum})"

    def transaction_count(self) -> int:
        return len(self.__transaction_collection)

    def __record_transaction(self, kind: str, amount: int | float) -> None:
        transaction = Transaction(kind, amount, f"{kind.title()} transaction")
        transaction.process_transaction()
        self.__transaction_collection.append(transaction)

    @staticmethod
    def valid_amount(amount: int | float, allow_zero: bool = False) -> bool:
        """Check for a finite number and allow zero when requested."""
        if type(amount) not in (int, float):
            return False
        if isinstance(amount, float) and not isfinite(amount):
            return False
        return amount >= 0 if allow_zero else amount > 0

    def deposit(self, amount: int | float) -> bool:
        """Add the amount and record the deposit.

        Return False and leave the balance and history unchanged.
        """
        try:
            if not self.valid_amount(amount):
                raise InvalidAmountError(
                    "Deposit amount must be a positive number."
                )
        except InvalidAmountError as error:
            print(error)
            return False
        self.__balance += amount
        self.__record_transaction("deposit", amount)
        return True

    def withdrawal(self, amount: int | float) -> bool:
        """Withdraw the amount and record the transaction.

        Return False without changing the balance or transaction history
        if the withdrawal is rejected.
        """
        try:
            self.valid_withdrawal(amount)
        except FinanceError as error:
            print(error)
            return False

        # Wait for the account checks before changing the balance.
        self.__balance -= amount
        self.__record_transaction("withdrawal", amount)
        return True

    @abstractmethod
    def valid_withdrawal(self, amount: int | float) -> bool:
        """Check the amount and balance before any account rules.

        Raise InvalidAmountError for an invalid amount or
        WithdrawalError if the balance is too low.
        """
        if not self.valid_amount(amount):
            raise InvalidAmountError(
                "Withdrawal amount must be a positive number."
            )
        if amount > self.Balance:
            raise WithdrawalError(
                f"Account {self.AccountNum} has a balance of {self.Balance}; "
                f"it cannot withdraw {amount}."
            )
        return True
