
class Transaction:
    def __init__(self, type, amount, description, status = "pending"):
        self.type = type
        self.amount = amount
        self.description = description
        self.status = status

    def new_description(self, description):
        self.description = description

    def confirm_transfer(self,account):
        if self.type == "deposit":
            account.deposit(self.amount)
            self.status = "Processed"
        elif self.type == "withdrawal":
            account.withdrawal(self.amount)
            if self.balance >= self.amount:
                self.status = "Processed"
        
        else:
            self.cancelled_state()

        

    def cancelled_state(self):
        self.status = "Cancelled"

    def display_transaction(self):
        print(self.type, self.amount, self.description, self.status)


