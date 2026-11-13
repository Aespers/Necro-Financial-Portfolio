
class Transaction:
    def __init__(self, type: str, amount: int|float, description: str, status = "pending"):
            self.__type = type if isinstance(type, str) and type.strip() else print("Type is error, please try again")
            self.amount = amount if isinstance(amount, (int, float)) else print("Amount is error, please try again")
            self.__description = description if isinstance(description, str) and description.strip() else print("Description is error, please try again")
            self.status = status


    def __str__(self) -> str:
        return f"{self.__type},{self.amount},{self.__description},{self.status}"

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description) -> None:
        if isinstance(description, str) and description.strip():
            self.__description = description
        else:
            print("Description should be in string! Try again.")

    def process_transaction(self) -> None:
        self.status = "Processed"

    def cancel_transaction(self) -> None:
        self.status = "Cancelled"

    def display_transaction(self) -> None:
        print(self.__type, self.amount, self.__description, self.status)


