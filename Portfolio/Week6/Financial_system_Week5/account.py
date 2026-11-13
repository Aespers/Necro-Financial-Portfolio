from transaction import Transaction


class Account:
    def __init__(self, account_num: int, account_type: str, balance: int | float, client_num: int) -> None:
        self.__account_num = (account_num if isinstance(account_num, int)
                              else print("Account name is error, please try again"))
        self.__account_type = (account_type if isinstance(account_type, str) and account_type.strip()
                               else print("Account type is error, please try again"))
        self.__balance = (balance if isinstance(balance, (int, float))
                          else print("Account name is error, please try again"))
        self.__client_num = (client_num if isinstance(client_num, int)
                             else print("Client number is error, please try again"))
        self.transaction_collection = []

    def get_account_num(self) -> int:
        return self.__account_num

    def get_account_type(self) -> str:
        return self.__account_type

    def get_balance(self) -> int | float:
        return self.__balance

    def get_client_num(self) -> int:
        return self.__client_num

    def get_transaction_collection(self) -> list:
        return self.transaction_collection

    AccountNum = property(get_account_num)
    AccountType = property(get_account_type)
    Balance = property(get_balance)
    ClientNum = property(get_client_num)
    TransactionCollection = property(get_transaction_collection)

    def __str__(self) -> str:
        transactions = ""
        for i in self.transaction_collection:
            transactions += f"{i}\n"
        return f"{self.__account_num},{self.__account_type},{self.__balance},{self.__client_num}\n Transaction collection:\n{transactions}"

    # Helper method to add a transaction record to transaction collection, takes the parameter and add it to the list.
    def transaction_record(self, transaction: Transaction) -> None:
        if not isinstance(transaction, Transaction):
            print("Only Transaction objects can be added!")
        else:
            self.transaction_collection.append(transaction)

    # Deposits money into account, calls transaction, and add the transaction record to the list after the transaction
    def deposit(self, amount: int | float) -> None:
        if isinstance(amount, (int, float)):
            self.amount = amount
            self.__balance = self.__balance + self.amount

            deposit_transaction = Transaction(
                "deposit",
                self.amount,
                "Deposit transaction",
            )

            deposit_transaction.process_transaction()
            self.transaction_record(deposit_transaction)
            self.display_account()

        else:
            print("Deposit amount should be an int")

    # Withdrawal money into account, calls transaction, and add the transaction record to the list after the transaction
    def withdrawal(self, amount: int | float) -> None:
        if isinstance(amount, (int, float)):
            self.amount = float(amount)

            if self.__balance < self.amount:
                print("Insufficient amount!")

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
            print("Withdrawal amount should be an int")

    def display_account(self) -> None:
        print("Account number: ", self.__account_num, "\n",
              "Account type: ", self.__account_type, "\n",
              "Balance: ", self.__balance, "\n",
              "Client number: ", self.__client_num
              )
