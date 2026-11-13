class Branch:
    def __init__(self, branch_num, branch_name, location, phone_num, status = "closed"):
        self.branch_num = branch_num
        self.branch_name = branch_name
        self.location = location
        self.phone_num = phone_num
        self.status = status

    def open_branch(self):
        self.status = "opened"
        print("The branch is now", self.status)

    def close_branch(self):
        self.status = "closed"
        print("The branch is now", self.status)

    def update_phone(self, phone_num):
        self.phone_num = phone_num
        print("Update successful, branch phone number is now", self.phone_num)

    def display_branch(self):
        print(self.branch_name, self.branch_num, self.location, self.phone_num, self.status)


