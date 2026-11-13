from account import Account


class EverydayAccount(Account):
    """An account with a limit on each withdrawal."""

    WITHDRAWAL_LIMIT = 5000

    def valid_withdrawal(self, amount: int | float) -> bool:
        """Check the usual rules and the limit for one withdrawal."""
        if not super().valid_withdrawal(amount):
            return False
        if amount > self.WITHDRAWAL_LIMIT:
            print("You have exceeded the withdrawal limit.")
            return False
        return True
