from account import Account


class EverydayAccount(Account):

    WITHDRAWAL_LIMIT = 5000

    def __init__(self, account_num: int, account_type: str, balance: int | float, client_num: int) -> None:
        super().__init__(account_num, account_type, balance, client_num)
