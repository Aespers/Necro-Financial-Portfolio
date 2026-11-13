class Account:
    def __init__(self, account_num: int, account_type: str, balance:int|float , client_num: int) -> None:
        self.__account_num = (account_num if isinstance(account_num, int)
                              else print("Account name is error, please try again"))
        self.__account_type = (account_type if isinstance(account_type, str) and account_type.strip()
                              else print("Account type is error, please try again"))
        self.balance = (balance if isinstance(balance, (int, float))
                              else print("Account name is error, please try again"))
        self.client_num = (client_num if isinstance(client_num, int)
                              else print("Client number is error, please try again"))



    def __str__(self) -> str:
        return f"{self.__account_num}:{self.__account_type}:{self.balance}:{self.client_num}"

    def deposit(self, amount: int|float) -> None:
        if isinstance(amount, (int, float)):
            self.amount = amount
            self.balance = self.balance + self.amount
            self.display_account()
        else:
            print("Deposit amount should be an int")

    def withdrawal(self, amount) -> None:
        if isinstance(amount, (int, float)): 
            self.amount = float(amount)
            if self.balance < self.amount:
                print("Insufficient amount!")
            else:
                self.balance = self.balance - self.amount
            self.display_account()
        else:
            print("withdrawal amount should be an int")


    def display_account(self) -> None:
        print("Account number: ", self.__account_num,"\n",
              "Account type: ", self.__account_type,"\n",
              "Balance: ", self.balance, "\n",
              "Client number: ", self.client_num
              )
