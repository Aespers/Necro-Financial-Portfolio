from branch import Branch
from account import Account


class Client:
    """Keep a client's contact details and accounts."""

    def __init__(
        self, client_num: int, name: str, phone_num: str,
        date_of_join: str, age: int, active: bool,
        preferred_branch: Branch | None = None
    ) -> None:
        if type(client_num) is not int or client_num <= 0:
            raise ValueError("Client number must be a positive integer.")
        if not all(
            isinstance(value, str) and value.strip()
            for value in (name, phone_num, date_of_join)
        ):
            raise ValueError("Name, phone and join date are required.")
        if type(age) is not int or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        if type(active) is not bool:
            raise ValueError("Active must be a boolean.")
        if preferred_branch is not None and not isinstance(
            preferred_branch, Branch
        ):
            raise ValueError("Preferred branch must be a Branch object.")
        self.__client_num = client_num
        self.__name = name
        self.__phone_num = phone_num
        self.__date_of_join = date_of_join
        self.__age = age
        self.__active = active
        self.__preferred_branch = preferred_branch
        self.__accounts: dict[int, Account] = {}

    def __str__(self) -> str:
        return (f"{self.ClientNum},{self.Name},{self.__phone_num},"
                f"{self.DateOfJoin},{self.Age},{self.__active},"
                f"{self.PreferredBranch}")

    def __repr__(self) -> str:
        return f"Client(client_num={self.ClientNum})"

    def add_account(self, account) -> None:
        if not isinstance(account, Account):
            print("Only Account objects can be added!")
        elif account.ClientNum != self.__client_num:
            print("This account belongs to a different client!")
        elif account.AccountNum in self.__accounts:
            print("This account number is already registered!")
        else:
            self.__accounts[account.AccountNum] = account

    def get_account(self, account_num: int) -> Account | None:
        if type(account_num) is not int:
            return None
        return self.__accounts.get(account_num)

    def get_contact(self) -> str:
        return "The phone number is " + self.__phone_num

    def set_contact(self, phone_num) -> None:
        if isinstance(phone_num, str) and phone_num.strip():
            self.__phone_num = phone_num
        else:
            print("Phone number should be a string! Try again.")

    def get_preferred_branch(self) -> Branch | None:
        return self.__preferred_branch

    def get_client_num(self) -> int:
        return self.__client_num

    def get_name(self) -> str:
        return self.__name

    def get_date_of_join(self) -> str:
        return self.__date_of_join

    def get_age(self) -> int:
        return self.__age

    def set_preferred_branch(self, preferred_branch) -> None:
        if isinstance(preferred_branch, Branch):
            self.__preferred_branch = preferred_branch
        else:
            print("Preferred branch should be a Branch object")

    Contact = property(get_contact, set_contact)
    PreferredBranch = property(get_preferred_branch, set_preferred_branch)
    ClientNum = property(get_client_num)
    Name = property(get_name)
    DateOfJoin = property(get_date_of_join)
    Age = property(get_age)
