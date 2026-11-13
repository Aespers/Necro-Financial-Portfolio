from math import isfinite


class Transaction:
    """Record the amount, description and status of a transaction."""

    def __init__(
        self, transaction_type: str, amount: int | float, description: str,
        status: str = "pending"
    ) -> None:
        if (not isinstance(transaction_type, str)
                or not transaction_type.strip()):
            raise ValueError("Transaction type is required.")
        if (type(amount) not in (int, float) or amount <= 0
                or isinstance(amount, float) and not isfinite(amount)):
            raise ValueError("Transaction amount must be a positive number.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Transaction description is required.")
        if status not in ("pending", "Processed", "Cancelled"):
            raise ValueError("Unknown transaction status.")
        self.__type = transaction_type
        self.__amount = amount
        self.__description = description
        self.__status = status

    def __str__(self) -> str:
        return (f"{self.__type},{self.__amount},"
                f"{self.__description},{self.__status}")

    def __repr__(self) -> str:
        return f"Transaction({self.Type!r}, {self.Amount!r})"

    def get_amount(self) -> int | float:
        return self.__amount

    def get_type(self) -> str:
        return self.__type

    def get_status(self) -> str:
        return self.__status

    Amount = property(get_amount)
    Type = property(get_type)
    Status = property(get_status)

    def get_description(self) -> str:
        return self.__description

    Description = property(get_description)

    def set_description(self, description) -> None:
        if isinstance(description, str) and description.strip():
            self.__description = description
        else:
            print("Description should be in string! Try again.")

    def process_transaction(self) -> None:
        self.__status = "Processed"

    def cancel_transaction(self) -> None:
        self.__status = "Cancelled"
