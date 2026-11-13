class Branch:
    """Represent a branch and its contact details."""

    def __init__(
        self, branch_num: int, branch_name: str, location: str,
        phone_num: str, status: str = "closed"
    ) -> None:
        if type(branch_num) is not int or branch_num <= 0:
            raise ValueError("Branch number must be a positive integer.")
        if not all(
            isinstance(value, str) and value.strip()
            for value in (branch_name, location, phone_num)
        ):
            raise ValueError("Branch name, location and phone are required.")
        if status not in ("opened", "closed"):
            raise ValueError("Unknown branch status.")
        self.__branch_num = branch_num
        self.__branch_name = branch_name
        self.__location = location
        self.__phone_num = phone_num
        self.__status = status

    def __str__(self) -> str:
        return (f"{self.BranchName}:{self.BranchNumber}:{self.Location}:"
                f"{self.PhoneNumber}:{self.Status}")

    def open_branch(self) -> None:
        self.__status = "opened"
        print("The branch is now", self.__status)

    def close_branch(self) -> None:
        self.__status = "closed"
        print("The branch is now", self.__status)

    def get_phone_num(self) -> str:
        return self.__phone_num

    def set_phone_num(self, phone_num) -> None:
        if isinstance(phone_num, str) and phone_num.strip():
            self.__phone_num = phone_num
            print("Updated branch phone number:", self.__phone_num)
        else:
            print("Phone number should be a string! Try again.")

    def get_branch_num(self):
        return self.__branch_num

    def get_branch_name(self):
        return self.__branch_name

    def get_location(self):
        return self.__location

    def get_status(self):
        return self.__status

    PhoneNumber = property(get_phone_num, set_phone_num)
    BranchNumber = property(get_branch_num)
    BranchName = property(get_branch_name)
    Location = property(get_location)
    Status = property(get_status)

    def __repr__(self) -> str:
        return f"Branch(branch_num={self.BranchNumber})"
