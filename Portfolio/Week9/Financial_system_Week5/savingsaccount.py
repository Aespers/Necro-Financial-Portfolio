from account import Account


class SavingsAccount(Account):
    """An account that must keep a minimum balance after withdrawal."""

    MINIMUM_BALANCE = 1000

    def __init__(
        self, account_num: int, account_type: str, balance: int | float,
        client_num: int, interest_rate: float
    ) -> None:
        super().__init__(account_num, account_type, balance, client_num)
        if not self.valid_amount(interest_rate, allow_zero=True):
            raise ValueError("Interest rate must be a non-negative number.")
        self.__interest_rate = interest_rate

    def get_interest_rate(self) -> float:
        return self.__interest_rate

    InterestRate = property(get_interest_rate)

    def valid_withdrawal(self, amount: int | float) -> bool:
        """Check that enough money will remain after the withdrawal."""
        if not super().valid_withdrawal(amount):
            return False
        if self.Balance - amount < self.MINIMUM_BALANCE:
            print("The account would fall below the minimum balance.")
            return False
        return True
