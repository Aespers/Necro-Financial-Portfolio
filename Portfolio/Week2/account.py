class Account:
    def __init__(self, account_num, account_type, balance, client_number):
        self.account_num = account_num
        self.account_type = account_type
        self.balance = balance
        self.client_number = client_number


    def deposit(self, amount):
        self.amount = amount

        # adds value to the balance
        self.balance = self.balance + self.amount
        self.display_account()

    def withdrawal(self, amount):
        self.amount = amount

        if self.balance < self.amount:
            print("Insufficient amount!")
        else:
            self.balance = self.balance - self.amount
        self.display_account()


    def display_account(self):
        print("Account number: ", self.__account_num,"\n",
              "Account type: ", self.account_type,"\n",
              "Balance: ", self.balance, "\n",
              "Client number: ", self.client_number
              )
