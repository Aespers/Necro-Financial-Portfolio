class Branch:
    def __init__(self, branch_num: int, branch_name: str, location: str, phone_num: str, status = "closed") -> None:
        self.branch_num = (branch_num if isinstance(branch_num, int)
                            else print("Branch number is error, please try again."))
        self.branch_name = (branch_name if isinstance(branch_name, str) and branch_name.strip()
                            else print("Branch name is error, please try again."))
        self.location = (location if isinstance(location, str) and location.strip()
                            else print("Location is error, please try again."))
        self.__phone_num = (phone_num if isinstance(phone_num, str) and phone_num.strip()
                            else print("Phone number is error, please try again."))
        self.status = status


    def __str__(self) -> str:
        return f"{self.branch_name}:{self.branch_num}:{self.location}:{self.__phone_num}:{self.status}"

    def open_branch(self) -> None:
        self.status = "opened"
        print("The branch is now", self.status)

    def close_branch(self) -> None:
        self.status = "closed"
        print("The branch is now", self.status)

    def get_phone(self) -> str:
        return self.__phone_num

    def set_phone(self, phone_num) -> None:
        if isinstance(phone_num, str) and phone_num.strip():
            self.__phone_num = phone_num
            print("Update successful, branch phone number is now", self.__phone_num)
        else:
            print("Phone number should be a string! Try again.")

    def display_branch(self) -> None:
        print(self.branch_name, self.branch_num, self.location, self.__phone_num, self.status)


