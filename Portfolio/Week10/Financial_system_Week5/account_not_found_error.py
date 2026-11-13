from finance_error import FinanceError


class AccountNotFoundError(FinanceError):
    """The client does not hold the account."""
