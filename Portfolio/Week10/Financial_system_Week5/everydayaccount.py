from account import Account
from withdrawal_error import WithdrawalError


class EverydayAccount(Account):
    """An account with a limit on each withdrawal."""

    WITHDRAWAL_LIMIT = 5000

    def valid_withdrawal(self, amount: int | float) -> bool:
        super().valid_withdrawal(amount)
        if amount > self.WITHDRAWAL_LIMIT:
            raise WithdrawalError(
                f"Account {self.AccountNum} cannot withdraw {amount}; "
                f"the limit is {self.WITHDRAWAL_LIMIT}."
            )
        return True
