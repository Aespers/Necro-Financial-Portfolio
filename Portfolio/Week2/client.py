
class Client:
    def __init__(self, client_num, name, phone_num, dateOfJoin, age, active):
        self.client_num = client_num
        self.name = name
        self.phone_num = phone_num
        self.dateOfJoin = dateOfJoin
        self.age = age
        self.active = active


    def change_contact(self, phone_num):
        self.phone_num = phone_num


    def display_client(self):
        print("Client number: ", self.client_num,"\n",
              "Client name: ", self.name,"\n",
              "Phone number: ", self.phone_num,"\n",
              "Date of join: ", self.dateOfJoin,"\n",
              "Age: ", self.age, "\n")

        if self.active == True:
            print("Account status: Active")
        else:
            print("Account status: Deactivated")
