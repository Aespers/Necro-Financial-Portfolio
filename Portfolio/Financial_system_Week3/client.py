from branch import Branch
from account import Account

class Client:
    def __init__(self, client_num: int, name: str, phone_num: str, dateOfJoin: str, age: int, active: bool, preferred_branch = None) -> None:
            self.__client_num = client_num if isinstance(client_num, int) else print("Client number is error, please try again.")
            self.__name = name if isinstance(name, str) and name.strip() else print("Name is error, please try again")
            self.__phone_num = phone_num if isinstance(phone_num, str) and phone_num.strip() else print("Phone number is error, please try again")
            self.__dateOfJoin = dateOfJoin if isinstance(dateOfJoin, str) and dateOfJoin.strip() else print("Date of join is error, please try again")
            self.__age = age if isinstance(age, int) else print("Age is error, please try again")
            self.active = active
            self.__preferred_branch = preferred_branch
            self.__accounts = []


    def __str__(self) -> str:
        return f"{self.__client_num}:{self.__name}:{self.__phone_num}:{self.__dateOfJoin}:{self.__age}:{self.active}:{self.__preferred_branch}"

    def add_account(self, account) -> None:
        if not isinstance(account, Account):
            print("Only Account objects can be added!")
        elif account.client_num != self.__client_num:
            print("This account belongs to a different client!")
        elif account not in self.__accounts:
            self.__accounts.append(account)


    def get_contact(self) -> str:
        return "The phone number is " + self.__phone_num

    def set_contact(self, phone_num) -> None:
        if isinstance(phone_num, str) and phone_num.strip():
            self.__phone_num = phone_num
        else:
            print("Phone number should be a string! Try again.")


    def set_branch(self, preferred_branch) -> None:
        if isinstance(preferred_branch, Branch):
            self.__preferred_branch = preferred_branch
        else:
            print("Preferred branch should be a Branch object")


    def display_client(self) -> None:
        print("Client number: ", self.__client_num,"\n",
              "Client name: ", self.__name,"\n",
              "Phone number: ", self.__phone_num,"\n",
              "Date of join: ", self.__dateOfJoin,"\n",
              "Age: ", self.__age, "\n")

        if self.active:
            print("Account status: Active")
        else:
            print("Account status: Deactivated")
