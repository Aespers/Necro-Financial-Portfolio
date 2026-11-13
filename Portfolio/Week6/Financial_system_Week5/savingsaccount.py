from account import Account


class SavingsAccount(Account):

    MINIMUM_BALANCE = 1000

    def __init__(self, account_num: int, account_type: str, balance: int | float, client_num: int, interest_rate: float) -> None:
        super().__init__(account_num, account_type, balance, client_num)
        self.__interest_rate = (interest_rate if isinstance(interest_rate, float)
                                else print("Interest rate is error, please try again"))

    def get_interest_rate(self):
        return self.__interest_rate

    InterestRate = property(get_interest_rate)
