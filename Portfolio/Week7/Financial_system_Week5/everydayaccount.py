from Week7.Financial_system_Week5.account import Account
from Week7.Financial_system_Week5.transaction import Transaction


class EverydayAccount(Account):

    WITHDRAWAL_LIMIT = 5000

    def __init__(self, account_num: int, account_type: str, balance: int | float, client_num: int) -> None:
        super().__init__(account_num, account_type, balance, client_num)

    def withdrawal(self, amount: int | float) -> None:
        pass

    def withdrawal(self, amount: int | float) -> None:
        if isinstance(amount, (int, float)) and amount >= 0:
            self.amount = float(amount)

            if self.__balance < self.amount:
                print("Insufficient amount!")

            elif self.amount > self.WITHDRAWAL_LIMIT:
                print("You have exceeded the withdrawal limit of ",
                      self.WITHDRAWAL_LIMIT)

            else:
                self.__balance = self.__balance - self.amount

                withdrawal_transaction = Transaction(
                    "withdrawal",
                    self.amount,
                    "Withdrawal transaction",
                )
                withdrawal_transaction.process_transaction()
                self.transaction_record(withdrawal_transaction)
            self.display_account()

        else:
            print("Withdrawal amount should be a positive number")
